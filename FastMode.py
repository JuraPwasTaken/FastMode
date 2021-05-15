#FastMode
version="3.0"
#Created by Jura Perić

#Libraries
from random import choice, randint
import sys
import base64
from time import sleep

#Variables and lists
allCharacters=["q","w","e","r","t","y","u","i","o","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",",",".","-","_","1","2","3","4","5","6","7,","8","9","0"]
finalPassword=""
charStore=[]
passSatisfaction=False
#version="{}-sys:{}".format(version, sys.platform)
passFileName="passlist"

#Definitions
def askUser(): #Asks the user to write/read
    while True:
        userInput=input("\nMake (M) or read (R) passwords: ")
        if userInput=="M" or userInput=="m":
            makePassword()
        elif userInput=="R" or userInput=="r":
            readPassword()

def makePassword(): #Function that makes the password
    charStore=[]
    passwordName=input("Enter password name: ")

    while True:
        for i in range(randint(10,40)): #randomly generate a password
            charStore.append(allCharacters[randint(0, len(allCharacters)-1)]) #temporarily store all generated characters in a list
        finalPassword="{}: {}".format(passwordName,"".join(charStore)) #make the password with its tag to potentially save 
        print(finalPassword)

        userInput=input("\nIs this password OK? (Y/N) (C to cancel): ")

        if userInput=="N" or userInput=="n": 
            print("Okay.")

        elif userInput=="C" or userInput=="c":
            print("Okay.")
            break;

        elif userInput=="Y" or userInput=="y":
            print("Okay. Your password {} has been saved.".format("".join(charStore)))

            if sys.platform=="win32": #checks if the system is a Windows PC
                passwrite=open("C:\FastMode\{}.txt".format(passFileName), "a") 

            else: #else if the system is a Mac or Linux PC
                passwrite=open("{}.txt".format(passFileName), "a")

            finalPassword="{}{}".format("GoBack", finalPassword)
            passBytes=finalPassword.encode("ascii")
            b64Bytes=base64.b64encode(passBytes)
            b64Pass=b64Bytes.decode("ascii")
            passwrite.write("{}".format(b64Pass))
            passwrite.close()
            charStore=[]
            break;

def readPassword(): #read all passwords
    print("Checking for your passwords. Please wait...")
    if sys.platform=="win32":
        passread=open("C:\FastMode\{}.txt".format(passFileName), "r")

    elif sys.platform=="darwin" or "linux":
        passread=open("{}.txt".format(passFileName), "r")
    toDecode=passread.read()
    b64Bytes=toDecode.encode("ascii")
    passBytes=base64.b64decode(b64Bytes)
    toPrint=passBytes.decode("ascii")
    if toPrint.find("GoBack")>=0:
        toPrint=toPrint.replace("GoBack","\n")

    print(toPrint)

#Execution
def main():
    print("FastMode, version {}, created by Jura Perić".format(version))
    if sys.platform=="win32":
        askUser()
    elif sys.platform=="darwin":
        print("Hello! macOS is currently not supported. Make it happen by contributing code to FastMode's GitHub page!\n>>> https://github.com/JuraPwasTaken/FastMode/ <<<")
        sleep(5)
        exit()
    elif sys.platform=="linux":
        print("Hello! Linux distros are currently not supported. Make it happen by contributing code to FastMode's GitHub page!\n>>> https://github.com/JuraPwasTaken/FastMode/ <<<")
        sleep(5)
        exit()
main()