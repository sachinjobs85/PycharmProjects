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
for measurement in results.get_points(measurement='healthCheck'):
    method = measurement['last']
    HealthState = measurement['HealthState']
    #fqdn = measurement['fqdn']
    # serverr = measurement['server']
    # responseTime = measurement['responseTime']
    # statusCode = measurement['statusCode']
    print(method, end=' ')
    print(HealthState, end=' ')
    #print(fqdn, end=' ')
    # print(serverr, end=' ')
    # print(responseTime, end=' ')
    # print(statusCode)

    with open('output.txt', 'w') as f:
        # for line in total:
        timestr = time.strftime("%Y-%m-%d %H:%M")
        f.write(timestr + " " + method + " " + HealthState)
        print("Done !!")
