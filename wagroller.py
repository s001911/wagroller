import random
import argparse

parser = argparse.ArgumentParser(description='Basic Wrath & Glory Dice Roller')
parser.add_argument('n',  type=int, help='Amount of Dice to be rolled')
parser.add_argument('-d',  type=int, default=3,  help='Difficulty Number, defaults to 3')
parser.add_argument('-r',  help='Show Dice Rolls',  action='store_true')

args = parser.parse_args()

#grab args
num = int(args.n)
dn = args.d

#Set master variables
complications = 0
icons = 0
exaltedIcons = 0
doneGlory = False
rolls = ""

#main loop
for i in range(0,  num) :
    roll = random.randint(1, 6)
    
    #determine if we need to do glory
    if (not doneGlory) :
        #force glory on last roll so there is always a glory.
        if (random.randint(1, num) == 1) or (i == num - 1) :
            #As far as I'm aware you can only have 1 special dice, so only do it once.
            doneGlory = True     
                        
            #Determine Wrath or Glory
            if (roll == 1) :
                hasGlory = "Wrath"
            elif (roll == 6) :
                hasGlory = "Glory"
            else :
                hasGlory = "Neither"
            
            #Mark as special
            roll = str(roll) + '*'       
    
    #Do not need a comma before the first roll
    #I figured a long string would be easier to handle than printing an array
    if (i == 0) :
        rolls = str(roll)
    else :
        rolls += ", " + str(roll)
        
    #Determine if anything is special about the roll and add it to the respective count
    if (roll == 1) :
        complications += 1
    if (roll == 4 or roll == 5) :
        icons += 1
    if (roll == 6) :
        exaltedIcons += 1
        

#get total icons, exalted count as 2 icons
totalIcons = icons + (exaltedIcons * 2)
#Did we pass?
passed = totalIcons >= dn

#Only output rolls if needed
if (args.r) :
    print ("Rolls: " + rolls)
    
#Final output
print("Wrath or Glory: " + hasGlory)
print("Complications: " + str(complications))
print("Icons: " + str(icons))
print("Exalted Icons: " + str(exaltedIcons))
print("Total Icons/Passes: " + str(totalIcons))
print("Passed: " + str(passed))
