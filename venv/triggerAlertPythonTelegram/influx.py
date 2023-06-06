import sys
import time
from influxdb import InfluxDBClient
import requests
import json

TOKEN = "5558538416:AAGDhGDtwDOYl-69RgRfNu1JB7U2g6ffVqY"
chat_id = "5130182527"

client = InfluxDBClient(host='192.168.0.184', port=8086)
list_db = client.get_list_database()
db = client.switch_database('ESB')
results = client.query('select * from tuxx limit 1')

for measurement in results.get_points(measurement='tuxx'):
    method = measurement['Method']
    api = measurement['apiName']
    print(method, end=' ')
    print(api)




