from read_pizza import *
from helpers import *
import copy

pizza_file = 'example.in'

challenge_dict = read_pizza(pizza_file)

parameters = copy.deepcopy(challenge_dict['parameters'])
pizza = copy.deepcopy(challenge_dict['pizza'])

min_cells = 2*parameters['mips']
min_slices = factor_pairs(min_cells)

small_slices = []

for j in range(parameters['rows']):
    for i in range(parameters['cols']):
        for shape in min_slices:
            slice_corners = dict(xtl=i, ytl=j, xbr=i+shape[0]-1, ybr=j+shape[1]-1)
            print slice_corners
            if not validate_corners(parameters, slice_corners): continue
            
            slice = characterise_slice(pizza, slice_corners)
            
            if not slice['fresh']: continue
            if not validate_params(pizza, parameters, slice): continue
        
            print 'accepting slice'
            print slice_corners
        
            pizza = reserve_slice(pizza, slice_corners)
            
            small_slices.append(slice)







