#############
## Modules ##
#############

from random import random as rand, randint #rand can be used to generate a random float between 0 and 1
                                           #randit can be used to generate random integers

#############
## Classes ##
#############
class agent():

    ##X and Y##

    def __init__(self, environment, agents):    #Generates x and y coordinates between 0 and 99
        self._x = randint(0,99)
        self._y = randint(0,99)

        self.environment = environment
        self.store = 0

        self.agents = agents

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

    ## Functions ##

    def move(self):                                 #Moves agent in a random direction
                if rand() < 0.5:
                    self._x = (self._x + 1) % 100
                else:
                    self._x = (self._x - 1) % 100

                if rand() < 0.5:
                    self._y = (self._y + 1) % 100
                else:
                    self._y = (self._y - 1) % 100

    def distanceBetween(self1, self2):              #Calculates the distance between agents
        answer = ((self1._x - self2._x)**2) + ((self1._y - self2._y)**2)**0.5
        return answer
    

    def eat(self):                                  #Allows agents to 'eat' the environment
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

    def shareWithNeighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distanceBetween(agent)

            if distance <= neighbourhood:
               distSum = self.store + agent.store
               distAvg = distSum / 2
               self.store = distAvg
               agent.store = distAvg
    
