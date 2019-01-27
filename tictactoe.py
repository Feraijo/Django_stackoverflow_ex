import itertools
import numpy as np
import operator
from collections import Counter

shape = 3
xs = list(chr(x+65) for x in range(shape))
ys = [str(x) for x in range(1,shape+1)]
combs = [''.join(x) for x in itertools.product(xs, ys)]
field = np.empty((shape,shape), dtype=str)
coords = itertools.product(range(shape), range(shape))
mapp = {}
for comb in zip(combs, coords):
    mapp[comb[0]] = comb[1]
    
winCoords = list()
for i in range(shape):
    winCoords.append([(i, x) for x in range(shape)])
    winCoords.append([(x, i) for x in range(shape)])
winCoords.append([(x,x) for x in range(shape)])
winCoords.append([(x,shape-1-x) for x in range(shape)])

def checkIfWin(field):
    for c in winCoords:        
        if field[c[0]] == field[c[1]] == field[c[2]] != '':
            return True        
    return False

def getCounter(dic, counter, mx):    
    global field
    #mx = max(dic.items(), key=operator.itemgetter(1))[1] 
    for k, v in dic.items():
        if v == mx:
            for c in k:
                if field[c] != '':
                    continue
                counter[c] += 1
    

def compTurn(field):    
    if len(field[field==''])==shape**2:
        field[(1,1)] = computer
    elif len(field[field==''])==1:
        field[field==''] = computer
    else:
        chancesW = {}  
        chancesL = {}
        counter = Counter()
        for coord in winCoords:
            chancesW[tuple(coord)] = 0
            chancesL[tuple(coord)] = 0
            for c in coord:
                if field[c] == computer:
                    chancesW[tuple(coord)]  += 2
                    chancesL[tuple(coord)]  -= 2
                elif field[c] == player:
                    chancesW[tuple(coord)]  -= 2
                    chancesL[tuple(coord)]  += 2
                else:
                    chancesW[tuple(coord)]  += 1
                    chancesL[tuple(coord)]  += 1
        
        mL = max(chancesL.items(), key=operator.itemgetter(1))[1] 
        mW = max(chancesW.items(), key=operator.itemgetter(1))[1] 
        if mL - mW >= 2:
            getCounter(chancesL, counter, mL)
        elif mW - mL >= 2:
            getCounter(chancesW, counter, mW)
        else:
            getCounter(chancesW, counter, mW)
            getCounter(chancesL, counter, mL)        
                    
        mm = max(counter.items(), key=operator.itemgetter(1))[0] 
        field[mm] = computer      
    return field

print('X or 0?')
player = '' 
while (player != 'X' and player != '0'):
    player = input()
if player == 'X':
    computer = '0'
else:
    computer = 'X' 
print ('You have chosen the {0}\'s, computer is playing {1}\'s.'.format(player, computer))
 
# Main cycle
turn = 'X'
print(field)
while (True):
    print('%s-player turn.'%turn)
    if turn == computer:
        field = compTurn(field)
    else:
        pcoord = ''
        while (pcoord not in combs):
            pcoord = input().capitalize()        
            try:
                if field[mapp[pcoord]] != '':
                    pcoord = ''
                    print('Already occupied, try again.')        
            except:
                print('Wrong coords!')
                continue
        field[mapp[pcoord]] = turn
    print(field)
    if checkIfWin(field):
        print('%s wins!' % turn)
        break
    if len(field[field==''])==0:
        print ('Draw!')
        break
    
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'