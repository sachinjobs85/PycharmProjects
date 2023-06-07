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
results = client.query('select last(Method) as Method, apiName from tuxx')

for measurement in results.get_points(measurement='tuxx'):
    method = measurement['Method']
    api = measurement['apiName']
    # counter = measurement['counter']
    # ip = measurement['ip']
    # responseTime = measurement['responseTime']
    # statusCode = measurement['statusCode']
    print(method, end=' ')
    print(api, end=' ')
    # print(counter, end=' ')
    # print(ip, end=' ')
    # print(responseTime, end=' ')
    # print(statusCode)

    with open('output.txt', 'w') as f:
        # for line in total:
        timestr = time.strftime("%Y-%m-%d %H:%M")
        f.write(timestr + " " + method + " " + api)
        print("Done !!")
