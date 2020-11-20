from hashlib import sha512
from map import map


def main():
    """
    executes the program
    prints out your password for that website
    """
    inputList = getValues()
    sha512Hash = sha512HashUserInput(inputList)
    securityLevel = int(input('Security Level: '))
    myPassword = pAlgorithm(sha512Hash, securityLevel)
    print(myPassword)


def getValues():
    """
    get values from the user
    website = website to be used for (ex: Facebook, Github, Gmail)
    username = username/email/id for the account (ex: hackerman, hack@gmail.com, djangoUbuntu18AWSServer)
    secret = password. This stays the same for any password in any given website
    breaches = number of times your password for this account has been breached, this can be stored externally
    """
    print("=== Executing Palgorithm ===")
    website = input('Website: ')
    username = input('Username: ')
    secret = input('Secret: ')
    breaches = input('Breaches: ')
    return [website, username, secret, breaches]


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
    Valid securityLevel in this algorithm is from 1 to 2
    
    The following succeeding code is an example only
    Use your own Password Algorithm for security
    """
    sectionsha512Hash = sha512Hash[22:70]
    inverted512Hash = sha512Hash[::-1]
    myLongPassword = sha512Hex(sectionsha512Hash + " hello world " + inverted512Hash)
    myShorterPassword = alphanumeric(myLongPassword)
    if securityLevel == 1:
        length = 20
    elif securityLevel == 2:
        length = 128
    else:
        raise RuntimeError("Security Level must be 1 or 2")
    myPassword = myShorterPassword[:length]
    return myPassword

def alphanumeric(longHex):
    longHexList = getHexList(longHex)
    alphanumeric = ""
    for h in longHexList:
        alphanumeric += map[h]
    return alphanumeric

def getHexList(longHex):
    longHexList = []
    char = ""
    for h in longHex:
        char += h
        if len(char) == 2:
            longHexList.append(char)
            char = ""
    return longHexList

main()