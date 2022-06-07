from cryptography.fernet import Fernet

myKey = Fernet.generate_key()

#write to a file
with open('filekey.key', 'wb') as f:
    f.write(myKey)

print('new key generated!')