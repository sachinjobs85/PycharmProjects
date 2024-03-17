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
query = "select last(pendingUserRequesetCount), HealthState from healthCheck where (statsType='ThreadInfo' AND HealthState='HEALTH_WARN') AND time>now()-5m GROUP BY fqdn,server"
results = client.query(query)
# cpu_points = list(results.get_points(measurement='healthCheck'))

print(results)