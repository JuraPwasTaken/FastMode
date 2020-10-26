#FastMode
version="2.0"
#Created by Jura Perić

#modules
from random import*

#lists
allCharacters=["q","w","e","r","t","y","u","i","o","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",",",".","-","_","1","2","3","4","5","6","7,","8","9","0"]
generatedPassword=[]
currentPassword=[]

#variables
randPick=0
passwordName=""
isSatisfiedWithPassword=False
numCursor=0
numOfRuns=0
finalPassword=""

#main code
print("FastMode Passode Generator, version {}, created by Jura Perić".format(version))
while True:
    if numOfRuns>=1:
        isSatisfiedWithPassword=False
        numCursor=0
    print("")
    
#asks you what you wanna do, if you request to write it runs appropriate code
    userInput=input("Enter a name for your password: ")
    passwordName=userInput
    print("Generating a password... please wait...")
        
#generates a new password and asks the user for approval until they're satisfied
    while isSatisfiedWithPassword==False:
        for i in range(randint(20,50)):
            randPick=randint(0, 64)
            generatedPassword.append(allCharacters[randPick])
            #print(generatedPassword)
                
        print("")
        print("Here is your password:","".join(generatedPassword))
        print("")
            
        #this part of code just resets the generatedPassword list so passwords wouldn't link with eachother
        #also it saves the generated password to the currentPassword list
        for i in range(len(generatedPassword)-1):
            currentPassword.append(generatedPassword[numCursor])
            numCursor=numCursor+1
                
        for i in range(len(generatedPassword)-1):
            generatedPassword.remove(generatedPassword[0])
                
        questionSatisfactionWithPassword=input("Are you satisfied with your password? (Y/N) ")
            
        if questionSatisfactionWithPassword=="y" or questionSatisfactionWithPassword=="Y":
            print('Great! Your password for "{}" is {}. Should appear in your password file any moment.'.format(passwordName, "".join(currentPassword)))
            isSatisfiedWithPassword=True
            
        if questionSatisfactionWithPassword=="n" or questionSatisfactionWithPassword=="N":
            print("Okay then, back to the drawing board...")
            isSatisfiesWithPassword=False
            numCursor=0
            for i in range(len(currentPassword)-1):
                currentPassword.remove(currentPassword[0])
        #keeps track of the number of times the program has been run (resets on startup)
        numOfRuns=numOfRuns+1
    #hippity hoppity some random code is now my property
    f=open("A list of all your passwords.txt", "a")
    f.write("{}: {}\n".format(passwordName, "".join(currentPassword)))
    f.close()
    for i in range(len(currentPassword)-1):
            currentPassword.remove(currentPassword[0])
