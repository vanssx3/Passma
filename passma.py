import sys
import random
import os.path
import linecache

allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'
passlist = './passmaStorage.txt'
passwordStr = ""

def start(startInput):
    input1 = input("Enter gen to make a new password or list to see a saved password. ")
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
            found = False
            while found == False:
                passwordCheck = input("Enter your master password: ")
                masterLine = linecache.getline(passlist, 1)
                if (masterLine.strip() == "passmanuts" + passwordCheck):
                    found = True
                    print("Password accepted!")
                    addToList(passwordStr, passwordCheck)
                else:
                    print("Incorrect Password!")
            

def addToList(passwordStr, passwordCheck):
    loginInfo = input("Enter what website the password will be used for: ")
    usernameInfo = input("Enter your username or email for this login: ")

    with open("passmaStorage.txt", "a") as passlist:
        passlist.write("\n")
        passlist.write(loginInfo)
        passlist.write("\n")
        passlist.write(usernameInfo)
        passlist.write("\n")
        passlist.write(passwordStr + passwordCheck)
        passlist.write("\n")
        passlist.write("\n")
    print("Added to password list!")

def listPass(passlist):
    if(os.path.isfile(passlist) == False):
        createNewList("none")
    else:
        passwordCheck = input("Enter your master password: ")
        masterLine = linecache.getline(passlist, 1)
        if (masterLine.strip() == "passmanuts" + passwordCheck):
            print("Password accepted!")
            input2 = input("What account are you looking for? Enter the website: ")
            found = False
            infoPart = 0
            print(input2)
            with open('passmaStorage.txt','r') as passlist:
                for line in passlist:
                    line = line.replace('\n','')
                    if found == True:
                        if infoPart == 1:
                            print("Email/Username: " + line)
                        if infoPart == 2:
                            print("Password: " + line.removesuffix(passwordCheck))
                            raise SystemExit
                        infoPart = 2
                    if line == input2:
                        print("Account info for " + input2 + ":")
                        found = True
                        infoPart = 1
                failInput = ''
                while failInput != 'y':
                    while failInput != 'n':
                        failInput = input("Account not found. Would you like to retry? (y/n) ")
                        if failInput == 'y':
                            listPass('./passmaStorage.txt')
                        if failInput == 'n':
                            print("Failed to find account. Exiting...")
                            raise SystemExit
        else:
            print("Incorrect password!")
            listPass(passlist)
                        
                    
        
def createNewList(passwordStr):
    noFileInput = input("No password list found. Would you like to create one? (y/n) ")
    if noFileInput == 'y':
        masterPass = input("What do you want your master password to be? Be sure not to lose this!!! ")
        f = open("passmaStorage.txt", "w")
        f.write("passmanuts" + masterPass)
        f.close()
        print("Password list created!")
        if not (passwordStr == "none"):
            addToList(passwordStr, masterPass)
            print("Password added to list.")
        print("Exiting...")
        raise SystemExit    
    elif noFileInput == 'n':
        print("List not created. Exiting...")
        raise SystemExit
    else:
        print("Invalid response")
        createNewList(passwordStr)

input1 = start(input)

if input1 == 'gen':
    genPass()
elif input1 == 'list':
    listPass(passlist)
else:
    print("Invalid Response. Exiting...")
    raise SystemExit
