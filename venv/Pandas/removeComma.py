with open('newProcess.txt', 'r') as data:
    plaintext = data.read()

plaintext = plaintext.replace('  ', ',')
print(plaintext)
n = plaintext.split(",")
print(n[0:3])