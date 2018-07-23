import json
import time
import requests
import datetime
import postgresql

import os
from os import sys, path
import django

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rets_backend.settings")
django.setup()

from general.models import *
# from utils import send_email

def get_last_property_id(self, market):
    # compare property id for initial loading, compare last_updated_date for pulling updates
    connection = self.get_db_connection()
    if real:
        query = "SELECT open_time FROM {}_rates where base_currency_id={} and quote_currency_id = {} ORDER BY open_time DESC LIMIT 1"

    res = connection.prepare(query.format(exchange.lower(), base, quote))()
    connection.close()
    # default 2 years ago
    return int(res[0]['open_time'].timestamp()) if res else int(time.time()) - 2 * 365 * 24 * 60 * 60


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

def main():
    for market in markets:
        # get last property id for the market
        sql = "select * from {}_properties where property_id > '150049016' order by property_id limit 20000;".format(market, property_id)
        # update id
        # put them in database
        values = []
        placeholders = ', '.join(['%s'] * len(res[0]))
        columns = ', '.join(res[0].keys())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s ) ON CONFLICT DO NOTHING" % (table_name[4:], columns, placeholders)

        # copy records
        for ii in res:
            values.append(ii.values())
        cursor.executemany(sql, values)
        # get ids
        # get relavant photos, rooms, attributes for the _properties
        # make thread
        # put them in database
        sql = "select * from il_mred_photos where property_id in (​‘150025666’, ‘150025667’​);" 

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
