from hashlib import sha512


def main():
    """
    executes the program
    prints out your password for that website
    """
    inputList = getValues()
    sha512Hash = sha512HashUserInput(inputList)
    securityLevel = int(input('Security: '))
    myPassword = pAlgorithm(sha512Hash, securityLevel)
    print(myPassword)


def getValues():
    """
    get values from the user
    website = website to be used for (ex: Facebook, Github, Gmail)
    username = username/email/id for the account (ex: hackerman, hack@gmail.com, djangoUbuntu18AWSServer)
    secret = password. This stays the same for any password in any given website
    """
    website = input('Website: ')
    username = input('Username: ')
    secret = input('Secret: ')
    return [website, username, secret]


def sha512HashUserInput(inputList):
    """
    returns the hashed user input using sha512
    formats the inputs to be spaced out 
    """
    inputWithSpaces = " ".join(inputList)
    inputHashHex = sha512Hex(inputWithSpaces)
    return inputHashHex


def sha512Hex(string):
    """
    convert input into a hash using sha512
    returns string type
    """
    stringBytes = string.encode()
    stringsha512 = sha512(stringBytes)
    stringHex = stringsha512.hexdigest()
    return stringHex
    

def pAlgorithm(sha512Hash, securityLevel):
    """
    Password Algorithm
    returns your ACTUAL password
    Any algorithm that returns your password

    Must be simple enough so you won't forget
    Must be difficult enough so no one else can get it
    Must be deterministic

    securityLevel determines the length of the password to be returned
    Valid securityLevel in this algorithm is from 1 to 4
    
    The following succeeding code is an example only
    Use your own Password Algorithm for security
    """
    sectionsha512Hash = sha512Hash[22:70]
    inverted512Hash = sha512Hash[::-1]
    myLongPassword = sha512Hex(sectionsha512Hash + " hello world " + inverted512Hash)
    if securityLevel == 1:
        length = 6
    elif securityLevel == 2:
        length = 10
    elif securityLevel == 3:
        length = 20
    elif securityLevel == 4:
        length = 128
    else:
        raise RuntimeError("Security Level must be 1, 2, 3, or 4")
    myPassword = myLongPassword[:length]
    return myPassword

main()