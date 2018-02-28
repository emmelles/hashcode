def characterise_slice(pizza, corners):
    
    # pizza is an NxM list of lists
    # corners is a dictionary containing 4 keys, xtl, ytl, xbr, ybr
    # This function has dual utility which I don't love, but it returns 0 for overlapped slices
    
    xtl = corners['xtl']
    ytl = corners['ytl']
    xbr = corners['xbr']
    ybr = corners['ybr']
    
    n_t = 0
    n_m = 0

    for j in range(xtl, xbr+1):
        for i in range(ytl, ybr+1):
            if   pizza[i][j] == 'T': n_t += 1
            elif pizza[i][j] == 'M': n_m += 1
            elif pizza[i][j] ==  0 : return 0
    
    return dict(t=n_t, m=n_m, corners=corners)


def validate_slice(pizza, params, slice_dict):
    if params['mips'] > ing_dict['m'] or params['mips'] > ing_dict['t']: return False
    
    if ing_dict['m'] + ing_dict['t'] > params['maxc']: return False
    
    return True


def validate_corners(params, corners):
    if corners['xbr'] > params['cols'] : return False
    if corners['ybr'] > params['rows'] : return False
    if corners['xtl'] > params['cols'] : return False
    if corners['ytl'] > params['rows'] : return False
    else: return True


def count_cells(ing_dict):
    return ing_dict['t'] + ing_dict['m']
    

def reserve_slice(pizza, corners):
    # cells set to 0 are presumed to be taken by another slice
        
    xtl = corners['xtl']
    ytl = corners['ytl']
    xbr = corners['xbr']
    ybr = corners['ybr']
    
    for j in range(xtl, xbr+1):
        for i in range(ytl, ybr+1):
            pizza[i][j] = 0
    
    return pizza
    
    
def factor_pairs(n):
    
    factors = []
    for i in range(1, n+1):
        if n % i == 0: factors.append(i)
        
    factor_pairs=[]
    for i in factors:
        factor_pairs.append([i, 12/i])
        
    return factor_pairs


    