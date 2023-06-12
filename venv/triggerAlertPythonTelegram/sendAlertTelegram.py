import time
import requests
import os

TOKEN = "5558538416:AAGDhGDtwDOYl-69RgRfNu1JB7U2g6ffVqY"
chat_id = "5130182527"

if os.path.getsize('output.txt') != 0:
    print("Yes !!! file has something")

    # while True:
    data = open('output.txt')
    count = data.read()
    print(count)
    n = count.split(" ")
    print(n[0])
    print(n[2])
    timestr = time.strftime("%Y-%m-%d %H:%M")
    print("Current Date Time: " + " " + str(timestr))

    if n[3] == "HEALTH_WARN":
        print("Alert Triggered !!")
        msg_count = "Health Warn Alert :" + "\t" + str(count) + " " + "\U0001F631"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg_count}"
        print(requests.get(url).json())
        print(msg_count)
        open('output.txt', 'w').close()
        print("Now File is Empty")

else:
    print("file is empty")
