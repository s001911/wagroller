import random
import argparse

parser = argparse.ArgumentParser(description='Basic Wrath & Glory Dice Roller')
parser.add_argument('n',  type=int, help='Amount of Dice to be rolled')
parser.add_argument('-d',  type=int, default=3,  help='Difficulty Number, defaults to 3')
parser.add_argument('-r',  help='Show Dice Rolls',  action='store_true')

args = parser.parse_args()

num = int(args.n)
dn = args.d

complications = 0
icons = 0
exaltedIcons = 0
doneGlory = False
rolls = ""

for i in range(0,  num) :
    roll = random.randint(1, 6)
    
    if (not doneGlory) :
        if (random.randint(1, num) == 1) or (i == num - 1) :
            doneGlory = True     
                       
            if (roll == 1) :
                hasGlory = "Wrath"
            elif (roll == 6) :
                hasGlory = "Glory"
            else :
                hasGlory = "Neither"
                
            roll = str(roll) + '*'       
    
    if (i == 0) :
        rolls = str(roll)
    else :
        rolls += ", " + str(roll)
    if (roll == 1) :
        complications += 1
    if (roll == 4 or roll == 5) :
        icons += 1
    if (roll == 6) :
        exaltedIcons += 1
        

totalIcons = icons + (exaltedIcons * 2)

passed = totalIcons >= dn

if (args.r) :
    print ("Rolls: " + rolls)
print("Wrath or Glory: " + hasGlory)
print("Complications: " + str(complications))
print("Icons: " + str(icons))
print("Exalted Icons: " + str(exaltedIcons))
print("Total Icons/Passes: " + str(totalIcons))
print("Passed: " + str(passed))
