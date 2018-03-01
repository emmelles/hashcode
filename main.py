# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from classes import *
from helpers import *

# Reading file - filename will need editing for different runs:
with open("a_example.in","r") as filein:
    contents=filein.read().split('\n')[:-1]

# Reading unique values:
rows,cols,cars,nrides,startbonus,totsteps = [int(d) for d in contents[0].split()]

        


# Iterating to make bookings into list of lists:
bookings=[]
for i, entry in enumerate(contents[1:]):
        tempbooking = Booking(i,[int(d) for d in entry.split()])
        bookings.append(tempbooking)  
        
book1 = bookings[1]      
print book1.starty()

time = 0
carList = []
for i in range(0,cars):
    tempcar = Car()
    carList.append(tempcar)

print 'Number of cars: ' + str(len(carList))

def timestep():
    for car in carList:
        if car.free == True:
            bookings = sorted(bookings, key = lambda booking: distance_metric(car.x,car.y,booking.startx(),booking.starty()))
            car.booking
    return 1

def dropFailedBookings:
    
    return 0

bookings = sorted(bookings, key = lambda booking: distance_metric(2,2,booking.startx(),booking.starty()))

for b in bookings:
    print [b.startx(), b.starty()]