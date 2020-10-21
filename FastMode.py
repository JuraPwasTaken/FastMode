#FastMode
version="1.0"
#Created by Jura Perić

#modules
from random import*

#lists
allCharacters=["q","w","e","r","t","y","u","i","o","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M",",",".","-","_","1","2","3","4","5","6","7,","8","9","0"]
generatedPassword=[]

#variables
randPick=0
nameOfPassword=""

#main code
print("FastMode Passode Generator, version {}, created by Jura Perić".format(version))
while True:
    userInput=input("Press enter for password")
    if userInput=="" or userInput!="":
        for i in range(randint(20,50)):
            randPick=randint(0, 64)
            generatedPassword.append(allCharacters[randPick])
        print("")
        print("Here is your password:","".join(generatedPassword))
        print("")
    for i in range(len(generatedPassword)-1):
        generatedPassword.remove(generatedPassword[0])
