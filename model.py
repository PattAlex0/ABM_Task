# model.py

"""
Created by Alex Patterson (GitHub @ alxpttn)

Runs an Agent Based model for a predetermined number of iterations

Requires agentFramework.py and in.txt, as well as csv, matplotlib, and random modules

"""

# Instructions:
# Ensure that agentFramework.py and in.txt are in the same directory as model.py
# After running, two txt files should be given in same directory
# outE.txt saves the changed environment
# outA.txt saves how much data each agent collected

# Modules
import agentFramework as AF
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from random import random         

# Environment List - Holds values for the environment
environment = []

# Agents List - Holds values for each agent
agents = []

# Distance List - Holds distances between agents
agentsDistance = []     

# Number of Agents - How many agents are in the model
numOfAgents = 50

# Iterations - Number of times the behavioural loop is run
iterations = 100

# Neighbourhood - How close agents have to be to one another to be considered in the same location
neighbourhood = 20

# Import raster data for use as environment
input = open('in.txt', newline = '')
reader = csv.reader(input, quoting = csv.QUOTE_NONNUMERIC)

# Add raster data to environment list
for row in reader:
    '''
    Copies the csv data into the environment list
    '''
    
    rowlist = []
    for value in row:
        
        rowlist.append(value)

    environment.append(rowlist)

input.close()

# Create plot object for later use
fig = plt.figure(figsize = (7, 7))

ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

# Assign initial positions for each agent
for i in range(numOfAgents):
    
    agents.append(AF.agent(environment, agents, agentsDistance))

# Create animation and behaviour loop
def update(frame_number):
    '''
    Basis of animation
    Refreshes the environment graphic, enacts agent behaviours, and plots agents in new positions
    '''

    # Update plot per loop
    fig.clear()
    plt.ylim(0, 299)
    plt.xlim(0, 299)
    plt.imshow(environment)
        
    # Agent behaviour per loop
    for i in range(numOfAgents):
        agents[i].move()
        agents[i].eat()
        agents[i].vomit()
        agents[i].shareWithNeighbours(neighbourhood)
        agents[i].stealFromNeighbours(neighbourhood)

    # Plot agent position per loop
    for i in range(numOfAgents):
        plt.scatter(agents[i].x, agents[i].y)

# Generator Function
def genFunction(b = [0]):
    """
    Genates animaion for a predetermined number of steps
    """

    # Assign starting value for counter
    a = 0
    
    # Check if counter has surpassed number of given iterations
    while (a < iterations):

        # Add to counter each time the animation is run
        yield a
        a += 1

# Create animations
animation = anim.FuncAnimation(fig, update, repeat=False, frames = genFunction)
plt.show()

# Save the modified environment to a txt file
outputE = open('outE.txt', 'w')
outputE.write(str(environment))
outputE.close()

# Save report of collected data by agents to
# a txt file
outputA = open('outA.txt', 'w', newline = '')
AResults = []

for i in range(numOfAgents):
    AResults.append('Agent ' + str(i + 1) + ' collected ' + str(agents[i].store) + ' bits of data')

outputA.write(str(AResults))
outputA.close()

# Check full program ran successfully
print('Program successfully run.')
