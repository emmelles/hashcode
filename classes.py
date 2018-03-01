# -*- coding: utf-8 -*-

class Booking:
    def __init__(self, number, data):
        self.n = number
        self.data = data
        
class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.free = True
        self.targetx = 0
        self.targety = 0
        self.timeToFree = 0
#        self.journeysComplete = []
        
    def step(self):
        if self.timeToFree > 0:
            self.timeToFree -= 1
        elif self.timeToFree == 0 and self.free == False:
            self.x = self.targetx
            self.y = self.targety
            self.free = True