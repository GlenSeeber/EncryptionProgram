from cryptography.fernet import Fernet

def encrypt(myPath):
    #read a file
    with open(myPath, 'rb') as f:
        inData = f.read()

    outData = fernet.encrypt(inData)

    #write to a file
    with open(myPath, 'wb') as f:
        f.write(outData)

def decrypt(myPath):
    #read a file
    with open(myPath, 'rb') as f:
        inData = f.read()

    outData = fernet.decrypt(inData)

    #write to a file
    with open(myPath, 'wb') as f:
        f.write(outData)


# Get the Key
with open('filekey.key', 'rb') as f:
    myKey = f.read()

fernet = Fernet(myKey)

decrypt("filename.txt")