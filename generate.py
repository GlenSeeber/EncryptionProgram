from cryptography.fernet import Fernet

def main():
    myKey = Fernet.generate_key()

    #write to a file
    with open('filekey.key', 'wb') as f:
        f.write(myKey)

    #only add the output if this is being run on it's own
    if __name__ == '__main__':
        input('new key generated! \n\npress enter to continue')

main()