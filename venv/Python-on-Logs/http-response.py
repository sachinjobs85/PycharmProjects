import re

file = open("service.log","r")
n = file.read()

for line in n:
    print(line,end="")
#print(n)

    x = re.findall("200|30[0-9]|40[0-9]|50[0-9]", line)
    print(x[0])


