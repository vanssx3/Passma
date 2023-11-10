import sys
import random
import hashlib
import os.path


allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'
passlist = './passmaStorage.txt'
input1 = ""

def start():
    input1 = input("Enter Gen to make a new password or List to see a saved password. ")

def genPass():
    input2 = input("How big do you want it to be? 16 Characters or more is recommended. ")
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
            createNewList()
        else:
            addToList()
            

def addToList():
    loginInfo = input("Enter what website the password will be used for: ")
    usernameInfo = input("Enter your username or email for this login: ")
    
    print("Added to password list!")

def listPass():
    if(os.path.isfile(passlist) == False):
        createNewList()
    else:
        print("Coming soon :3")
    
def createNewList():
    noFileInput = input("No password list found. Would you like to create one? (y/n) ")
    if input1 == 'Gen':
        if noFileInput == 'y':
            addToList()
        elif noFileInput == 'n':
            print("Password not saved. Exiting...")
            raise SystemExit
        else:
            print("Invalid response")
            createNewList()
    if input1 == 'List':
        if noFileInput == 'y':
            # Create list
            print("Password List created. Add some passwords to list them!")
            raise SystemExit
        elif noFileInput == 'n':
            print("Absolutely nothing has been done! Exiting...")
            raise SystemExit
start()

if input1 == 'Gen':
    genPass()
elif input1 == 'List':
    listPass()
else:
    "Invalid Response"
    start()


