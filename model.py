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
numOfAgents = 10
iterations = 100

##Agent Movement##
for i in range(numOfAgents):
    #Assign 10 agents with x and y coordinates to agents list
    agents.append([randint(0, 100), randint(0, 100)])

for i in range(iterations):
    #Loop the next forloop for 100 iterations
    for i in range(numOfAgents):
        #Moves agent's y position randomly
        if random() < 0.5:
            agents[i][0] += 1
        else:
            agents[i][0] -= 1

        #If agent's y position is out of bounds, it is placed at the 'entrance' from the other boundary
        if agents[i][0] <0:
            agents[i][0] = 100
        if agents [i][0] >100:
            agents[i][0] = 0

        #Moves agent's x position randomly
        if random() < 0.5:
            agents[i][1] += 1
        else:
            agents[i][1] -= 1

        #If agent's x position is out of bounds, it is placed at the 'entrance' from the other boundary
        if agents[i][1] <0:
            agents[i][1] = 100
        if agents [i][1] >100:
            agents[i][1] = 0

##Graph##
#Set x and y limits for graph
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

#Plots each agent on the graph using a forloop
for i in range(numOfAgents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

#Colours the point furthest east black  
m = max(agents, key = itemgetter(1))
matplotlib.pyplot.scatter(m[1], m[0], color='black')
matplotlib.pyplot.show()


##Currently not in use##
#Calculates the distance between the two agents using Pythagoras' theorem
#answer = ((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2)**0.5
