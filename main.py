import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# take a password, and securely derive a random fernet key from it
# taken from fernet docs: 
# https://cryptography.io/en/latest/fernet/#using-passwords-with-fernet
def passwordToKey(password, salt = b''):

    password = password.encode('ascii')

    # if they don't pass salt in the function (or if they pass the wrong
    # bit size of salt), generate new salt
    if len(salt) != 16:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(

        algorithm=hashes.SHA256(),

        length=32,

        salt=salt,

        iterations=390000,
    )

    myKey = base64.urlsafe_b64encode(kdf.derive(password))

    #you need to keep the salt if you want to be able to derive the same
    #key from the password in the future (i.e. if you want to actually
    # be able to use the password to unlock stuff)
    return myKey, salt

def encrypt(myPath, fileName, myPass):
    # add a / to the end of the path if it's not already there
    myPath = fixPath(myPath)

    # save key and salt from the password, don't save the password.
    myKey, salt = passwordToKey(myPass)     # [debug] remember to add password

    # save salt
    with open(myPath+'salt.key', 'wb') as f:
        f.write(salt)

    # use key for fernet
    fernet = Fernet(myKey)

    # open input file
    with open(myPath+fileName, 'rb') as f:
        inData = f.read()

    # encrypt input data
    outData = fernet.encrypt(inData)

    #create unique file, paste encrypted data onto it
    writeNewFile(myPath, 'encrypted-output', extension='.nerd', content=outData)

def decrypt(myPath, fileName, myPass):
    # add a / to the end of the path if it's not already there
    myPath = fixPath(myPath)
    # find salt
    with open(myPath+'salt.key', 'rb') as f:
        salt = f.read()

    # find key using password and salt.
    myKey = passwordToKey(myPass, salt)[0]     # [debug] remember to add password and salt

    # use key for fernet
    fernet = Fernet(myKey)

    #if fileName is blank, use the default output name of the encrypt function
    if fileName == '':
        fileName = 'encrypted-output.nerd'
    
    # read input
    with open(myPath+fileName, 'rb') as f:
        inData = f.read()

    outData = fernet.decrypt(inData)

    #write to a file
    writeNewFile(myPath, 'decrypted-output', content=outData)

#creates a new file with a unique name, and writes content to it
def writeNewFile(myPath, fileName, extension='.zip', flags='b', content=''):
    n = -1
    suffix = ''
    running = True
    while running:
        try:
            fullPath = myPath+fileName+suffix+extension
            with open(fullPath, 'x'+flags) as f:
                f.write(content)

                running = False
                #the name of the full directory + file name
                return fullPath

        except:
            #increase the n counter until we get a unique filename
            n += 1
            # example: filename(0).zip
            suffix = '('+str(n)+')'



myPath = input("Directory to your file (including final /):\n> ")
fileName = input("The filename (including .zip) of your input file:\n> ")

operation = input("Decrypt or Encrypt (d/e):\n> ")

password = input('passcode:\n> ')

def fixPath(input):
    if input[-1] != '/':
        input += '/'
    return input

if operation == 'e':
    encrypt(myPath, fileName, password)

elif operation == 'd':
    decrypt(myPath, fileName, password)

else:
    print('error')