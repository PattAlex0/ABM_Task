##Modules##
from random import randint, random
    #randint can be used to produce a random integer
    #random can be used to produce a random number between 0 and 1

from operator import itemgetter
    #itemgetter can be used to select specific elements

import matplotlib.pyplot
    #Can be used to create graphs

##Values##
agents = []

agents.append([randint(0, 99), randint(0, 99)])
agents.append([randint(0, 99), randint(0, 99)])

print("Starting Positions: 0 =", agents[0][0], agents[0][1], ", 1 =", agents[1][0], agents[1][1])

##Function - 0##
#Moves agent 0 based on the outcome of the random function
if random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

if random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

##Function - 1##
#Moves agent 1 based on the outcome of the random function
if random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

if random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

if random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

##Output##
print("End Positions: 0 =", agents[0][0], agents[0][1], ", 1 =", agents[1][0], agents[1][1])

#Calculates the distance between the two agents using Pythagoras' theorem
answer = ((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2)**0.5
print("Distance =", answer)

##Graph##
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key = itemgetter(1)) #selects point furthest east
matplotlib.pyplot.scatter(m[1], m[0], color='red') #Colours the point furthest east red
matplotlib.pyplot.show()
