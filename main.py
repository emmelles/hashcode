# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from classes import *
from helpers import *

# Reading file - filename will need editing for different runs:
input_file = "c_no_hurry.in"
with open(input_file,"r") as filein:
    contents=filein.read().split('\n')[:-1]

# Reading unique values:
rows,cols,cars,nrides,startbonus,totsteps=[int(d) for d in contents[0].split()]




# Iterating to make bookings into list of lists:
bookings=[]
for i, entry in enumerate(contents[1:]):
        tempbooking=Booking(i,[int(d) for d in entry.split()])
        bookings.append(tempbooking)

taxis=[]
for i in range(cars):
    temp_car = Car()
    taxis.append(temp_car)


for time_step in range(totsteps+1):
    for taxi in taxis:
        if taxi.free:
            if not 'journeys' in taxi.__dict__.keys():
                taxi.journeys=[]
            available_bookings = filter(lambda x: (x.starttime()-distance_metric(taxi.x, taxi.y, x.fromx, x.fromy) <= time_step) & (x.endtime() >= time_step+x.distance()+distance_metric(taxi.x, taxi.y, x.fromx, x.fromy)), bookings)
            
            available_bookings = sorted(bookings, key=lambda x: distance_metric(taxi.x, taxi.y, x.fromx, x.fromy))
            
            if available_bookings:
                chosen_booking=available_bookings[0]
                booking_number=chosen_booking.bookingN
                taxi.journeys.append(booking_number)
                bookings = filter(lambda x: x.bookingN != booking_number, bookings)
                taxi.timeToFree = chosen_booking.distance() + distance_metric(taxi.x, taxi.y, chosen_booking.fromx, chosen_booking.fromy)
                taxi.free = False
        
        taxi.step()
            
for taxi in taxis:
    print taxi.journeys
    
output_file = input_file[:-2]+'out'

with open(output_file, 'w') as f:
    for i, taxi in enumerate(taxis):
        journeys = taxi.journeys
        print(journeys)
        output_line = [str(len(journeys))]
        for journey in journeys: output_line.append(str(journey))
        f.write(' '.join(output_line) + '\n')


