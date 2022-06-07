from cryptography.fernet import Fernet


def encrypt(myPath, fileName):
    #read a file
    with open(myPath+fileName, 'rb') as f:
        inData = f.read()

    outData = fernet.encrypt(inData)

    #create unique file
    writeNewFile(myPath, 'encrypted-output', content=outData)


def decrypt(myPath, fileName):
    #read a file
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


# Get the Key
try:
    # [debug] you could add a unit test here, it would remove the 
    # content from filekey.key/delete it, and then allow the except to run
    
    with open('filekey.key', 'rb') as f:
        myKey = f.read()
    
    if (len(myKey) <= 0):
        raise
#if the filekey.key is empty/doesn't exist, generate a new key
except:
    exec(open("generate.py").read())    #run our generate.py script
    print('no encryption key was found, a new one has been generated')  #debug message

    #actually open the file now that we did that, assign the value to myKey
    with open('filekey.key', 'rb') as f:
        myKey = f.read()


fernet = Fernet(myKey)

myPath = input("Directory to your file (including final /):\n> ")
fileName = input("The filename (including .zip) of your input file:\n> ")

operation = input("Decrypt or Encrypt (d/e):\n> ")

if operation == 'd':
    decrypt(myPath, fileName)

elif operation == 'e':
    encrypt(myPath, fileName)

else:
    print('error')