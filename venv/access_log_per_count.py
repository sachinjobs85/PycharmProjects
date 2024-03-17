import sys
import time
from influxdb import InfluxDBClient
import requests
import json

TOKEN = "5558538416:AAGDhGDtwDOYl-69RgRfNu1JB7U2g6ffVqY"
chat_id = "5130182527"

client = InfluxDBClient(host='192.168.29.133', port=8086)
list_db = client.get_list_database()
db = client.switch_database('zabbix')
query = "select * from (select count(uuid) from accessLog where time>now()-2h GROUP BY IP,fqdn,apiName,statusCode)"
results = client.query(query)
# cpu_points = list(results.get_points(measurement='healthCheck'))

print(results)
for measurement in results.get_points(measurement='accessLog'):
    print(measurement)