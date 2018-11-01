##Modules##
from random import randint, random
    #randint can be used to produce a random integer
    #random can be used to produce a random number between 0 and 1

##Values##
#Creates x and y coordinates (between 0 and 99) for two agents
x0 = randint(0, 99)
y0 = randint(0, 99)

x1 = randint(0, 99)
y1 = randint(0, 99)

print("Starting Positions: 0 =", x0, y0, ", 1 =", x1, y1)

##Function - 0##
#Moves agent 0 based on the outcome of the random function
if random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random() < 0.5:
    x0 += 1
else:
    x0 -= 1

if random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random() < 0.5:
    x0 += 1
else:
    x0 -= 1

##Function - 1##
#Moves agent 1 based on the outcome of the random function
if random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random() < 0.5:
    x1 += 1
else:
    x1 -= 1

if random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random() < 0.5:
    x1 += 1
else:
    x1 -= 1

##Output##
print("End Positions: 0 =", x0, y0, ", 1 =", x1, y1)

#Calculates the distance between the two agents using Pythagoras' theorem
answer = ((y0 - y1)**2) + ((x0 - x1)**2)**0.5
print("Distance =", answer)
