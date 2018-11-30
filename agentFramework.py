##Modules##
from random import random as rand, randint 

##Classes##
class agent():

    def __init__(self):
        self.x = randint(0,99)
        self.y = randint(0,99)

    def move(self):
                if rand() < 0.5:
                    self.x = (self.x + 1) % 100
                else:
                    self.x = (self.x - 1) % 100

                if rand() < 0.5:
                    self.y = (self.y + 1) % 100
                else:
                    self.y = (self.y - 1) % 100

    def distanceBetween(self1, self2):
        answer = ((self1.x - self2.x)**2) + ((self1.y - self2.y)**2)**0.5
        print(answer)
        return answer
        
