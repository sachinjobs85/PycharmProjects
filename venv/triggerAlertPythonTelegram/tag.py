import pandas as pd
from influxdb import InfluxDBClient

client = InfluxDBClient(host='192.168.29.133', port=8086)
list_db = client.get_list_database()
db = client.switch_database('ESB')
query = "select * from (select last(pendingUserRequesetCount), HealthState from healthCheck where (statsType='ThreadInfo' AND HealthState='HEALTH_WARN') GROUP BY fqdn,server)"

df = pd.DataFrame(client.query(query).get_points())
print(df)
