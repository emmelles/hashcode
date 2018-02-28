def sum_ings(pizza, corners):
    
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
            if pizza[i][j] == 'T': n_t += 1
            elif pizza[i][j] == 'M': n_m += 1
            else: return 0
    
    return dict(t=n_t, m=n_m)


def validate_slice(pizza, params, ing_dict):
    if params['mips'] > ing_dict['m'] or params['mips'] > ing_dict['t']: return False
    
    if ing_dict['m'] + ing_dict['t'] > params['maxc']: return False
    
    return True


def count_cells(ing_dict):
    return ing_dict['t'] + ing_dict['m']
    

def confirm_slice(pizza, corners):
    # cells set to 0 are presumed to be taken by another slice
        
    xtl = corners['xtl']
    ytl = corners['ytl']
    xbr = corners['xbr']
    ybr = corners['ybr']
    
    for j in range(xtl, xbr+1):
        for i in range(ytl, ybr+1):
            pizza[i][j] = 0
    
    return pizza