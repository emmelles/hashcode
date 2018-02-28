def read_pizza(filename):

    pizza_file = []
    
    with open(filename, 'r') as f:
        for line in f:
            pizza_file.append(line)
    
    
    parameters = pizza_file[0][:len(pizza_file[0])-1].split(' ')
    
    rows = int(parameters[0])
    cols = int(parameters[1])
    mips = int(parameters[2])
    maxc = int(parameters[3])
    
    pizza = []
    
    for line in pizza_file[1:]:
        pizza.append(list(line[:cols-1]))

    return dict(parameters=parameters, pizza=pizza)
    
# Example usage:
# pizza_dict = read_pizza('example.in')

