with open('newProcess.txt', 'r') as data:
    plaintext = data.read()

plaintext = plaintext.replace('  ', ',')
print(plaintext)
# plaintext1 = plaintext.replace('   ', ',')
# print(plaintext1)

with open('newProcess1.txt', 'w') as f:
    # timestr = time.strftime("%Y-%m-%d %H:%M")
    f.write(plaintext)
    print("Done !!")


#n = plaintext.replace()
