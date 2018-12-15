## Modules ##

#Agent Class
import agentFramework as AF

#Environment and Graphics
import csv
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#Other
from random import shuffle, random         
from operator import itemgetter

## Values ##

#Agent Lists
environment = []        #Holds values for the environment
agents = []             #Holds values for each agent
agentsDistance = []     #Holds distances between agents

#Iterables
numOfAgents = 50        #Number of agents
iterations = 100        #Number of times the movement loop is run
neighbourhood = 20      #Value which determines how close agents have to be to one another to be considered in the same location

##  Environment  ##

#Import raster data
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

#Add raster data to environment list
for row in reader:
    '''
    Copies the csv data into the environment list
    '''
    
    rowlist = []
    for value in row:
        
        rowlist.append(value)

    environment.append(rowlist)

f.close()

#Create plot object for later use
fig = plt.figure(figsize = (7, 7))

ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

## Agent Movement ##

# Assign initial positions for each agent
for i in range(numOfAgents):
    
    agents.append(AF.agent(environment, agents, agentsDistance))

#Create animation and movement loop
def update(frame_number):
    '''
    Movement direction is determined by use of random() function
    Modulus operater is used to divide each number by 299
    If any number goes to 299, it will have 0 remainders and so be assigned a 0 coordinate
    '''

    #Update plot per loop
    fig.clear()
    plt.ylim(0, 299)
    plt.xlim(0, 299)
    plt.imshow(environment)
        
    #Agent behaviour per loop
    for i in range(numOfAgents):
        agents[i].move()
        agents[i].eat()
        agents[i].vomit()
        agents[i].shareWithNeighbours(neighbourhood)

    #Plot agent position per loop
    for i in range(numOfAgents):
        plt.scatter(agents[i].x, agents[i].y)
        #print(agents[i].x, agents[i].y)

#Generator Function
def genFunction(b = [0]):
    """
    Genates animaion for a predetermined number of steps
    """
    a = 0
    while (a < 100):
        yield a
        a += 1

#Movement Animation
animation = anim.FuncAnimation(fig, update, repeat=False, frames = genFunction)
plt.show()
      
## Distance Loop ##
shuffle(agents)

for i in range(numOfAgents):
    agents[i].distanceCalculator()

print("Maximum distance = " + str(max(agents[i].agentsDistance)) +   #Prints the maximum and minimum distances
           ", Minimum distance = " + str(min(agents[i].agentsDistance)))
