#FastMode Installer
version="1.0ALPHA"
#Created by Jura Perić

#Libraries
import sys
import os
from time import sleep

#Execution
print("We detected that you're using a {} system.".format(sys.platform))

if sys.platform=="win32":
    newpath="C:\FastMode"
    os.makedirs(newpath)
    f=open("C:\FastMode\passlist.txt","w+")
    f.close()
    print("All done! Take your FastMode.py file out of the downloaded folder and place it where you please!")
    print("Contribute to FastMode's code here:\n>>> https://github.com/JuraPwasTaken/FastMode/ <<<")
    sleep(5)
    exit()

elif sys.platform=="darwin":
    print("Hello! macOS is currently not supported. Make it happen by contributing code to FastMode's GitHub page!\n>>> https://github.com/JuraPwasTaken/FastMode/ <<<")
    sleep(5)
    exit()

elif sys.platform=="linux":
    print("Hello! Linux distros are currently not supported. Make it happen by contributing code to FastMode's GitHub page!\n>>> https://github.com/JuraPwasTaken/FastMode/ <<<")
    sleep(5)
    exit()