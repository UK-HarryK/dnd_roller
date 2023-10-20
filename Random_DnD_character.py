charactername = input("Enter charactername:")
print("this character is called: " + charactername)

import random 

z = (random.randint(0, 1))
if z == 1:
    print("theyre male")
if z == 0:
    print("Theyre female")

x = (random.randrange(1, 4))
if x == 1:
    print("theyre an elf")
if x == 2:
    print("theyre a human")
if x == 3:
    print("theyre a tiefling")
if x == 4:
    print("theyre a dwarf")

b  = (random.randrange(1, 4))
if b == 1:
    print("and are a rogue class")
if b == 2:
    print("and are a warlock class")
if b == 3:
    print("and are a paladin class")
if b == 4:
    print("and are a bard class")

if b == 1:
    z = (random.randrange(1, 3))
    if z == 1:
        print("with the cutthroat subclass")
    if z == 2:
        print("with the assassin subclass")
    if z == 3:
        print("with the thief subclass")

if b == 2:
    z = (random.randrange(1, 3))
    if z == 1:
        print("with the fiend subclass")
    if z == 2:
        print("with the celestial subclass")
    if z == 3:
        print("with the fathomless subclass")

if b == 3:
    z = (random.randrange(1, 3))
    if z == 1:
        print("with the eldritch knight subclass")
    if z == 2:
        print("with the holy knight subclass")
    if z == 3:
        print("with the blood knight subclass")

if b == 4:
    z = (random.randrange(1, 3))
    if z == 1:
        print("with the College of Creation subclass")
    if z == 2:
        print("with the College of Eloquence subclass")
    if z == 3:
        print("with the College of lore subclass")

y = (random.randrange(1, 3)) 
if y == 1:
    y == ("abrasive")
if y == 2:
    y == print("absent minded")
if y == 3:
    y == ("aggressive")
print("they have a",(y),"personality")

        
        
        
        #Abrasiveness. Abrasiveness can be seen as a negative trait because it describes having trouble being nice in a conversation. ...

#Brawler. ...
#Cautious. ...
#Detached

# So just to add some notes, more for my own reference.
# This is a fantastic start, and a great example of how to logically work through a problem with multiple steps,
# particularly where they are dependant on prior results.
# However, as discussed, this is not very DRY (Don't Repeat Yourself), and there is some work we can do to make this more human readable
# and efficient. It is worth noting that python is not actually very efficient, it is quite a resource intensive language, so effciency here
# is more in regards to time to code.
# (obviously this is a passion and learning project so those are in quotes as they are completely arbitrary)