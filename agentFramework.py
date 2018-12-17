# agentFramework.py

"""
Created by Alex Patterson (GitHub @ alxpttn)

Creates the agent class, including its x and y features and behavioural functions

Requires random module
"""

# Instructions:
# To modify the possible x and y coordinates for all agents, change the randint range for self._x and self._y
# To modify the probabilty of movement, change the probability value in the move function
# To modify how much data an agent takes from the environment, change the store value in the eat function
# To modify how much data an agent steals from another agent, change the store values in the stealFromNeighbours function
# To modify how much data an agent must have before expunging, change the values in the vomit function

from random import random as rand, randint

#Agent Class
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

    #Define x and y positions as properties of the agents
    x = property(getx, setx, delx, 'The x coordinate of an agent.')
    y = property(gety, sety, dely, 'The y coordinate of an agent.')

    #Move function
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

    #Eat function
    def eat(self):
        """
        Allows agents to 'eat' the environment
        """

        #Determine if there is enough data to consume
        if self.environment[self.y][self.x] > 10:
            
            #Remove environment data
            self.environment[self.y][self.x] -= 10

            #Add data to agent's own store
            self.store += 10

        #Determine if there is any 'leftover' data
        elif self.environment[self.y][self.x] > 0:

            #Add leftover data to agent's store
            self.store += self.environment[self.y][self.x]

            #Remove all data from environment
            self.environment[self.y][self.x] = 0
            

    #Share function
    def shareWithNeighbours(self, neighbourhood):
        """
        Allows agents to share data with each other
        """

        #Create loop to assess all possible agents
        for agent in self.agents:

            #Calculate distance between other agents
            distance = self.distanceBetween(agent)

            #Check if any agent is close enough and if they have equal or more data
            if distance <= neighbourhood and agent.store >= self.store:

               #Add together data from both agents
               distSum = self.store + agent.store

               #Divide total by two
               distAvg = distSum / 2

               #Give dived total to both agents
               self.store = distAvg
               agent.store = distAvg

    #Steal function
    def stealFromNeighbours(self, neighbourhood):
       """
       Allows agents to steal data from other agents if the are low on food
       """
        
       #Create loop to assess all possible agents
       for agent in self.agents:

          #Calculate distance between other agents
          distance = self.distanceBetween(agent)

          #Check if any agent is close enough, if the current agent is low on data,
          #and if the other agent has a minium amount of data
          if distance <= neighbourhood and self.store <= 10 and agent.store >= 10:

              #Add 10 to the thief's store
              self.store += 10

              #Remove 10 from the agent who was robbed
              agent.store -= 10

    #Vomit function
    def vomit(self):
        """
        Forces agents to expunge data if they contain too much
        """

        #Check if agent has too much data
        if self.store > 100:
            
            #Remove 100 from agent's store
            self.store -= 100
            
            #Add 100 back into the environment
            #self.environment[self.y][self.x] += 100

    #Distance function
    def distanceBetween(self1, self2):
        """
        Calculates the distance between agents
        """

        #Calculate distance between agents using the pythygoras theorem
        answer = ((self1.x - self2.x)**2) + ((self1.y - self2.y)**2)**0.5
        return answer
