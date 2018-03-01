# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Reading file - filename will need editing for different runs:
with open("a_example.in","r") as filein:
    contents=filein.read().split('\n')[:-1]

# Reading unique values:
rows,cols,cars,nrides,startbonus,totsteps=contents[0].split()

        
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
    

# Iterating to make bookings into list of lists:
bookings=[]
for i, entry in enumerate(contents[1:]):
        tempbooking=Booking(i,entry.split())
        bookings.append(tempbooking)    
    
print bookings
