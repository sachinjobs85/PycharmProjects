from influxdb import InfluxDBClient
import os

db = InfluxDBClient(host='192.168.0.184', port=8086)
db.switch_database('test')

if os.path.getsize('removejunk.txt') == 0:
            print("File is empty!")
else:
    def read_data():
        with open('removejunk.txt') as f:
            return [x.split(',') for x in f.readlines()[0:]]


    a = read_data()
    print(a)
    print("Done")
    for metric in a:
        influx_metric = [{
            'measurement': 'processData',
            'time': metric[0],
            'fields': {
                'dateTime': metric[0],
                'host': metric[1],
                'user': metric[2],
                'junk1': metric[3],
                'junk2': metric[4],
                'status': metric[5],
                'diff': metric[6],
            }
        }]
        db.write_points(influx_metric)

        open('removejunk.txt', 'w').close()
        print("Now File is Empty")