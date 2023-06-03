import time

while True:
    print("Hello Sachin")
    print("This is you first docker images")
    print("All the Best !!!")
    time.sleep(3)
    print("==============Done==============")

    with open(r"process.txt", 'r') as fp:
        for line in fp:
            print(line)