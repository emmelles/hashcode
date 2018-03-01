file = open('pizza_in/example.in','r')
print 'File contents:'
print file.read()
file.seek(0)
values = file.readline().split()
toppings = file.read()
file.close

print 'Toppings:\n' + toppings
#for number in values:
#    print number + '\n',
rows = int(values[0])
columns = int(values[1])
minT = int(values[2])
maxA = int(values[3])
pizza = toppings.split()
mask = []
row = []
slices = []

#To get around immutable lists and their copies...
for y in range(0,columns):
        row.append(0)
for x in range(0,rows):
    mask.append(list(row))
#Note: watch when making temporary masks not to reference the same object

#slice components: r1,c1,r2,c2
    
def maxSlices():
    mush,toms = whatsonmyslice([0,0,rows,columns])
    return min(mush/minT,toms/minT)

def whatsonmyslice(slice):
    r1 = slice[0]
    r2 = slice[2]
    c1 = slice[1]
    c2 = slice[3]
    sliceArray = [0]*(r2-r1)
    for r in range(r1,r2):
        sliceArray[r-r1] = pizza[r][c1:c2]
    sliceTop = ''
    for line in sliceArray:
        sliceTop += line
    mushrooms = sliceTop.count('M')
    tomatoes = sliceTop.count('T')
#    print sliceTop
    return [mushrooms,tomatoes]

def isTopped(slice):
    tops = whatsonmyslice(slice)
    if tops[0] >= minT and tops[1] >= minT:
        return True
    else: return False
    
def isTooBig(slice):
    x = slice[2] - slice[0]
    y = slice[3] - slice[1]
    if (x*y) > maxA:
        return True
    else: return False
    
def isValid(slice):
    if not isTooBig(slice) and isTopped(slice) and not overlaps(slice):
        return True
    else: return False
    
def overlaps(slice):
    r1 = slice[0]
    r2 = slice[2]
    c1 = slice[1]
    c2 = slice[3]
    for r in range(r1,r2):
        if max(mask[r][c1:c2]) > 0:
            return True
    else: return False
    
def setMask(slice):
    r1 = slice[0]
    r2 = slice[2]
    c1 = slice[1]
    c2 = slice[3]
    for r in range(r1,r2):
        for c in range(c1,c2):
            mask[r][c] = 1

def resetMask(slice):
    r1 = slice[0]
    r2 = slice[2]
    c1 = slice[1]
    c2 = slice[3]
    for r in range(r1,r2):
        for c in range(c1,c2):
            mask[r][c] = 0
            
def limitTopping():
    mush,toms = whatsonmyslice([0,0,rows,columns])
    if mush < toms: return 'M'
    else: return 'T'
    
def unLimitTopping():
    lim = limitTopping()
    if lim == 'T': return 'M'
    else: return 'T'
    
def nextLimit(rs,cs):
    limit = limitTopping()
    found = False
    rf = rs
    while rf < rows:
        cf = cs
        while cf < columns:
            if pizza[rf][cf] == limit:
                found = True
                return [rf,cf]
                break
            else: cf += 1
        if found: break
        else: rf += 1
    if not found: return [-1,-1]
    
def cutmeaslice(rs,cs):
    return 1
    
topAll = whatsonmyslice([0,0,rows,columns])
print 'Mushrooms: ' + str(topAll[0])
print 'Tomatoes: ' + str(topAll[1])
print 'Max. slices: ' + str(maxSlices())
print nextLimit(0,2)