#FastMode for macOS
version="2.1"
#Created by Jura Perić

#modules
from random import*

#lists
allCharacters=["q","w","e","r","t","y","u","i","o","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",",",".","-","_","1","2","3","4","5","6","7,","8","9","0"]
generatedPassword=[]

#variables
randPick=0
passwordName=""
isSatisfiedWithPassword=False
numOfRuns=0
numOfPassGens=0

#functions
def generatePassword():
    for i in range(randint(20,50)):
            randPick=randint(0, len(allCharacters)-1)
            generatedPassword.append(allCharacters[randPick])

#main code
print("FastMode Passcode Generator, version {}, created by Jura Perić\n".format(version))
while True:
    if numOfRuns>=1:
        isSatisfiedWithPassword=False
        numCursor=0
    
#asks you what you wanna do, if you request to write it runs appropriate code
    userInput=input('\nEnter "R" to read your passwords or "W" to make a new one: ')

    #Write
    if userInput.find("W")>=0 or userInput.find("w")>=0:
        userInput=input("Enter a name for your password: ")
        passwordName=userInput
        print("Generating a password... please wait...")
        
        #generates a new password and asks the user for approval until they're satisfied
        while isSatisfiedWithPassword==False:

            while numOfPassGens==0:
                generatePassword()
                numOfPassGens=numOfPassGens+1
        
            print("\nHere is your password:","".join(generatedPassword),"\n")
                
            questionSatisfactionWithPassword=input("Are you satisfied with your password? (Y/N) ")
            
            if questionSatisfactionWithPassword=="n" or questionSatisfactionWithPassword=="N":
                print("Okay then, back to the drawing board...")
                generatedPassword=[]
                generatePassword()

            elif questionSatisfactionWithPassword=="y" or questionSatisfactionWithPassword=="Y":
                print('Great! Your password for "{}" is {}. Should appear in your password list any moment.'.format(passwordName, "".join(generatedPassword)))
                isSatisfiedWithPassword=True

            else:
                print("Sorry, I didn't quite catch that.")
            
            #keeps track of the number of times the program has been run (resets on startup)
            numOfRuns=numOfRuns+1
    
        #saves the password in the password list document
        f=open("passlist.txt", "a")
        f.write("\n{}: {}".format(passwordName, "".join(generatedPassword)))
        f.close()


    #Read
    if userInput.find("R")>=0 or userInput.find("r")>=0:
        print("Checking your password file. Please wait...")
        f=open("passlist.txt", "r")
        print(f.read())
