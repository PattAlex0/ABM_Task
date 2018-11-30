#############
## Modules ##
#############

import agentFramework as AF

from operator import itemgetter            #itemgetter can be used to select specific elements

from time import clock                     #clock can be used to see how long a program takes to run

import matplotlib.pyplot as pyp            #Can be used to create graphs

###################
## Timer - Start ##
###################

timeStart = clock()     #Starting value of timer

############
## Values ##
############

## Lists ##
agents = []             #Holds values for each agent
agentsDum = []          #Holds values for each agent; only used within loop
agentsDistance = []     #Holds distances between agents

## Iterables ##
numOfAgents = 10        #Number of agents
iterations = 100        #Number of times the movement loop is run

####################
## Agent Movement ##
####################

## Initial Assignment ##
for i in range(numOfAgents):    #Assigns starting x and y values for each agent.
    agents.append(AF.agent())

## Movement Loop ##
for i in range(iterations):     #Movement direction is determined by use of random() function
                                #Modulus operater is used to divide each number by 100; if any number goes to 100, it will have 0 remainders and so be assigned a 0 coordinate  
    for i in range(numOfAgents):
        
        agents[i].move()
        
            
###################
## Distance Loop ##
###################

## Distance Calculator Loop ##            
for i in range(numOfAgents):    #Calculates the distance between each agent using the distanceBetween function
                                #Repeated agents are skipped over by adding them to the agentsDum list, which is checked in the loop
    agentsDum.append(i)

    for j in range(numOfAgents):
        if j in agentsDum:
            continue
        else:
            agents[i].distanceBetween(agents[j])
            agentsDistance.append(agents[i].distanceBetween(agents[j]))

## Distance Printer ##
print("Maximum distance = " + str(max(agentsDistance)) +   #Prints the maximum and minimum distances
      ", Minimum distance = " + str(min(agentsDistance)))

#################                  
## Timer - End ##
#################

timeEnd = clock()                          #Ending value of timer
print("Time = ", str(timeEnd - timeStart)) #Prints the total time taken for the program to run

###########
## Graph ##
###########

## Graph Coordinates ##
pyp.ylim(0, 99)           #Set x and y limits for graph
pyp.xlim(0, 99)

## Agent Plotting ##
for i in range(numOfAgents):            #Plots each agent on the graph
    pyp.scatter(agents[i].x,agents[i].y)

## Maximum Colour ## 
#m = max(agents, key = itemgetter(1))    #Colours the point furthest east black  
#pyp.scatter(m[1], m[0], color='black')

## Display Graph##
pyp.show()
