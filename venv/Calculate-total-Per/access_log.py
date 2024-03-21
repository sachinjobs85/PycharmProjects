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
query = "select * from (select count(uuid) from accessLog where (statusCode=~/20[0-9]/ OR statusCode=~/50[0-9]/) AND time>now()-10h GROUP BY IP,fqdn,apiName)"
results = client.query(query)
query2 = "select * from (select count(uuid) from accessLog where (statusCode='500') AND time>now()-10h GROUP BY IP,fqdn,apiName,statusCode)"
results2 = client.query(query2)
# cpu_points = list(results.get_points(measurement='healthCheck'))

print(results)
print(results2)
for measurement1 in results.get_points(measurement='accessLog'):
    # for measurement2 in results2.get_points(measurement='accessLog'):
    #     #print(measurement2)
    #     IP = measurement2['IP']
    #     apiName = measurement2['apiName']
    #     fqdn = measurement2['fqdn']
    #     statusCode = measurement2['statusCode']
    #     count = measurement2['count']
    #     print(IP, end=' ')
    #     print(apiName, end=' ')
    #     print(fqdn, end=' ')
    #     print(statusCode, end=' ')
    #     print(count)

    IP = measurement1['IP']
    apiName = measurement1['apiName']
    fqdn = measurement1['fqdn']
    #statusCode = measurement1['statusCode']
    count = measurement1['count']
    print(IP, end=' ')
    print(apiName, end=' ')
    print(fqdn, end=' ')
    #print(statusCode, end=' ')
    print(count)

with open('query1.txt', 'w') as f:
        # for line in total:
    timestr = time.strftime("%Y-%m-%d %H:%M")
    f.write(timestr + " " + str(IP) + " " + apiName + " " + fqdn + " " + str(count))
    print("Done !!")

# for measurement2 in results2.get_points(measurement='accessLog'):
#         #print(measurement2)
#     IP = measurement2['IP']
#     apiName = measurement2['apiName']
#     fqdn = measurement2['fqdn']
#     statusCode = measurement2['statusCode']
#     count = measurement2['count']
#     print(IP, end=' ')
#     print(apiName, end=' ')
#     print(fqdn, end=' ')
#     print(statusCode, end=' ')
#     print(count)
#
#     with open('query2.txt', 'w') as f:
#         # for line in total:
#         timestr = time.strftime("%Y-%m-%d %H:%M")
#         f.write(timestr + " " + str(IP) + " " + apiName + " " + fqdn + " " + str(statusCode) + " " + str(count))
#         print("Done !!")