import pandas as pd
import time
import os
from influxdb import InfluxDBClient

df = pd.read_csv(r'txtprocess.txt', skiprows=0)
print(len(df))

last_row = pd.DataFrame(df)
df2 = df.iloc[[-1]]
#print(df2)

new_last_row_dateTime = (df2['dateTime'].iloc[0])
print("Latest Event date&Time: " + new_last_row_dateTime)

if os.path.getsize('finalCountprocess.txt') == 0:
            print("File is empty!")
else:
    print("File has something")
file = open("finalCountprocess.txt")
last_row_date = file.read()
old_last_date_time = last_row_date
print("File has this old date&Time: " + old_last_date_time)

df.set_index('dateTime', inplace=True)
df.index = pd.to_datetime(df.index)

match_timestamp = str(new_last_row_dateTime)
match_timestamp1 = str(old_last_date_time)
n = df.loc[(df.index.strftime("%Y-%m-%d %H:%M:%S") <= match_timestamp) & (df.index.strftime("%Y-%m-%d %H:%M:%S") > match_timestamp1)]
print(n)
print(len(n))
print("Done !!!")

if len(n) == 0:
    print("No new data is available")
else:
    print("Data is Available")
    with open('newProcess.txt', 'w') as f:
        # timestr = time.strftime("%Y-%m-%d %H:%M")
        f.write(str(n))
        print("New data save as a csv Formet!!!!!!")


with open('finalCountprocess.txt', 'w') as f:
    # timestr = time.strftime("%Y-%m-%d %H:%M")
    f.write(str(new_last_row_dateTime))
    print("Done !!")
