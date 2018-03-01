# -*- coding: utf-8 -*-

from helpers import *

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
            
            
class Booking:
    
    def __init__(self,bookingN,data):
        self.data = data
        self.bookingN=bookingN
        self.fromx = data[0]
        self.fromy = data[1]
        self.tox = data[2]
        self.toy = data[3]
        self.beginning = data[4]
        self.ending = data[5]
    
    # One by one getters    
    def bookingN(self):
        return self.bookingN
        
    def startx(self):
        return self.fromx
    
    def starty(self):
        return self.fromy
    
    def endx(self):
        return self.tox
    
    def endy(self):
        return self.endy
    
    def starttime(self):
        return self.beginning
    
    def endtime(self):
        return self.ending

    # Pair getters        
    def startcoord(self):
        return [self.fromx,self.fromy]

    def endcoord(self):
        return [self.tox,self.toy]
    
    def timecoords(self):
        return [self.beginning,self.ending]
    
    # distance and whatnot
    def distance(self):
        return distance_metric(self.fromx, self.fromy, self.tox, self.toy)

