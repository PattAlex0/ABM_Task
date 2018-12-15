## Modules ##
from random import random as rand, randint

## Classes ##
class agent():
    """
    An agent for use in the model
    Contains a modifiable x and y position
    An agent can interact with the environment and other agents
    """

    #Initialisation
    def __init__(self, environment, agents, agentsDistance):
        """
        Generates x and y coordinates between 0 and 299
        """

        #Generate x and y positios
        self._x = randint(0, 299)
        self._y = randint(0, 299)

        #Connect to global environment list
        self.environment = environment

        #Create empty store
        self.store = 0

        #Connect to global agents list
        self.agents = agents

        #Connect to global distance list
        self.agentsDistance = agentsDistance


    def getx(self):
        return self._x
    def gety(self):
        return self._y

    def setx(self, value):
        self._x = value
    def sety(self, value):
        self._y = value

    def delx(self):
        del self._x
    def dely(self):
        del self._y

    x = property(getx, setx, delx, 'The x coordinate of an agent.')
    y = property(gety, sety, dely, 'The y coordinate of an agent.')

    #Functions
    def move(self):
        """
        Moves agent in a random direction
        """

        #X Movement
        if rand() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299

        #Y movement
        if rand() < 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299
    
    def eat(self):
        """
        Allows agents to 'eat' the environment
        """
        if self.environment[self.y][self.x] > 10:
            
            #Remove environment data
            self.environment[self.y][self.x] -= 10

            #Add data to agent's own store
            self.store += 10

    def shareWithNeighbours(self, neighbourhood):
        """
        Allows agents to share data with each other
        """
        for agent in self.agents:

            #Calculate distance between other agents
            distance = self.distanceBetween(agent)

            #Threshold checker
            if distance <= neighbourhood:

               #Add together data from both agents
               distSum = self.store + agent.store

               #Divide total by two
               distAvg = distSum / 2

               #Give dived total to both agents
               self.store = distAvg
               agent.store = distAvg

    def vomit(self):
        """
        Forces agents to expunge data if they contain too much
        """

        if self.store > 100:
            
            self.store -= 100
            
            self.environment[self.y][self.x] += 100

    def distanceBetween(self1, self2):
        """
        Calculates the distance between agents
        """
        
        answer = ((self1.x - self2.x)**2) + ((self1.y - self2.y)**2)**0.5
        return answer

    def distanceCalculator(self):
        '''
        Calculates the distance between each agent using the distanceBetween function
        Repeated agents are skipped over by adding them to the agentsDum list, which is checked in the loop
        '''

        #Create dummy list
        agentsDum = []

        #Append each agent to dummy list
        agentsDum.append(self)

        for agent in self.agents:

            #Check if agent has already been looked at
            if agent in agentsDum:
                continue

            #Append each distance value to the global distance list
            else:
                self.agentsDistance.append(self.distanceBetween(agent))


        
