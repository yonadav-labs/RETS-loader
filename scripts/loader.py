import json
import time
import thread
import requests
import datetime
import postgresql

import os
from os import sys, path
import django
from django.db import connection as conn_rets

conn_wolf = get_db_connection()

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rets_backend.settings")
django.setup()

from general.models import *
# from utils import send_email

def get_last_property_id(self, market):
    # compare property id for initial loading, compare last_updated_date for pulling updates
    lp = Property.objects.filter(id__startswith=market).orderby('-id').first()
    return lp.id if lp else ''


markets = [
    'ca_mlslistings',
    'ca_mrmls',
    'ca_claw',
    'ca_ebrd',
    'ca_crisnet',
    'ca_bear',
    'ca_sfar',
    'ca_bareis',
    'hi_hbr'
]

def dictfetchall(cursor, market, key='id'):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    result = []
    
    for row in cursor.fetchall():
        ii = dict(zip(columns, row))
        ii[key] = '{}_{}'.format(market, ii.pop('property_id'))
        result.append(ii)
    return result


def main():
    num_result = 1
    while num_result:
        for market in markets:
            # get last property id for the market
            property_id = get_last_property_id(market)

            with conn_wolf.cursor() as cursor:
                sql = "select * from {}_properties where property_id > '{}' order by property_id limit 20000;".format(market, property_id)
                cursor.execute(sql)
                res = dictfetchall(cursor, market)

            if res:
                num_result += len(res)
                with conn_rets.cursor() as cursor:
                    values = []
                    ids = []
                    placeholders = ', '.join(['%s'] * len(res[0]))
                    columns = ', '.join(res[0].keys())
                    sql = "INSERT INTO property ( %s ) VALUES ( %s ) ON CONFLICT DO NOTHING" % (columns, placeholders)

                    # copy records
                    for ii in res:
                        values.append(ii.values())
                        ids.append(ii['id'].split('_')[-1])
                    cursor.executemany(sql, values)

                    # get relavant photos, rooms, attributes for the _properties
                    # make thread
                    for ii in ['photos', 'property_attributes', 'property_rooms']:
                        thread.start_new_thread(save_models, (market, ii, ids,))


def save_models(market, table, ids):
    with conn_wolf.cursor() as cursor:
        sql = "select * from {}_{} where property_id in {};".format(market, table, tuple(ids))
        cursor.execute(sql)
        res = dictfetchall(cursor, market, 'property_id')
    
    with conn_rets.cursor() as cursor:
        placeholders = ', '.join(['%s'] * len(res[0]))
        columns = ', '.join(res[0].keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON CONFLICT DO NOTHING" % (table, columns, placeholders)

        values = []
        for ii in res:
            values.append(ii.values())
        cursor.executemany(sql, values)


def get_db_connection(self):
    config = {
        "DB": {
            "DATABASE": "wolfnet_data_services",
            "USER": "agent_cloud",
            "PASSWORD": "^u/P3aEL",
            "HOST": "provisioning2.wolfnet.com",
            "PORT": "6432",
        }    
    }

    conn_str = 'pq://{}:{}@{}:{}/{}'.format(self.config['DB']['USER'], self.config['DB']['PASSWORD'],
                                            self.config['DB']['HOST'], self.config['DB']['PORT'],
                                            self.config['DB']['DATABASE'])
    connection = postgresql.open(conn_str)
    return connection    


if __name__ == "__main__":
    main()
