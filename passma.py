import sys
import random
import hashlib
import os.path


allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'
passlist = './passmaStorage.txt'
passwordStr = ""

def start(startInput):
    input1 = input("Enter Gen to make a new password or List to see a saved password. ")
    return input1


def genPass():
    input2 = input("How big do you want the password to be? 16 Characters or more is recommended. ")
    passwordStr = ""
    for x in range(0, (int(input2))):
        passwordStr = passwordStr + allChars[random.randint(0, (len(allChars) - 1))]
    print(passwordStr)
    input3 = input("Would you like to add this to your password list? (y/n) ")
    if input3 == 'n':
        print("Password not saved. Exiting...")
        raise SystemExit
    if input3 == 'y':
        if(os.path.isfile(passlist) == False):
            createNewList(passwordStr)
        else:
            addToList(passwordStr)
            

def addToList(passwordStr):
    loginInfo = input("Enter what website the password will be used for: ")
    usernameInfo = input("Enter your username or email for this login: ")
    with open("passmaStorage.txt", "a") as f:
        f.write(loginInfo)
        f.write("\n")
        f.write(usernameInfo)
        f.write("\n")
        f.write(passwordStr)
        f.write("\n")
    print("Added to password list!")

def listPass():
    if(os.path.isfile(passlist) == False):
        createNewList()
    else:
        print("Coming soon :3")
    
def createNewList(passwordStr):
    noFileInput = input("No password list found. Would you like to create one? (y/n) ")
    if input1 == 'Gen':
        if noFileInput == 'y':
            f = open("passmaStorage.txt", "w")
            f.close()
            addToList(passwordStr)
        elif noFileInput == 'n':
            print("Password not saved. Exiting...")
            raise SystemExit
        else:
            print("Invalid response")
            createNewList(passwordStr)
    if input1 == 'List':
        if noFileInput == 'y':
            # Create list
            print("Password List created. Add some passwords to list them!")
            raise SystemExit
        elif noFileInput == 'n':
            print("Absolutely nothing has been done! Exiting...")
            raise SystemExit

input1 = start(input)

if input1 == 'Gen':
    genPass()
elif input1 == 'List':
    listPass()
else:
    "Invalid Response"


