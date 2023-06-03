# file = open('newProcess.txt')
# n = file.read()
# print(n[1:])

# list to store file lines
lines = []
# read file
with open(r"newProcess.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"newProcess.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [0, 1]:
            n = fp.write(line)
            print(lines)

with open('newProcess.txt', 'r') as data:
    plaintext = data.read()

plaintext = plaintext.replace('  ', ',')
print(plaintext)
# plaintext1 = plaintext.replace('   ', ',')
# print(plaintext1)

with open('removejunk.txt', 'w') as f:
    # timestr = time.strftime("%Y-%m-%d %H:%M")
    f.write(plaintext)
    print("Done !!")

