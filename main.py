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
