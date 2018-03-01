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

# Iterating to make bookings into list of lists:
bookings=[]
for i, entry in enumerate(contents[1:]):
    bookings.append([])
    for j in entry:
        # Strip spurious spaces:
        if j is not " ": bookings[i].append(j)

class booking:
    
    def __init__(self, bookingN,fromx,fromy,tox,toy,beginning,end):
        self.bookingN=bookingN
        self.fromx = fromx
        self.fromy = fromy
        self.tox = tox
        self.toy = toy
        self.beginning = beginning
        self.end = end
        
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
    
    def beginning(self):
        return self.beginning
    
    def end(self):
        return self.end
        
    def startcoord(self):
        return [self.fromx,self.fromy]

    def endcoord(self):
        return [self.tox,self.toy]
    
    def timecoords(self):
        return [self.beginning,self.end]
    

# This how you use
print contents[1].split()
mybooking=booking(1,0,0,1,3,2,9)
print mybooking.end()