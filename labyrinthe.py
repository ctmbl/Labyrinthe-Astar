import sys
import math

import ipdb
import time



def move(start, path):
    for p in path:#[::-1]:
        #print('\n\n')
        for row in world.get_carte():
            print(row)
        #input('')
        time.sleep(0.05)
        mv =  (p[0]-start[0], p[1]-start[1])
        start = p
        if mv == (0,1):
            world.move_kirk('DOWN')
#            print('DOWN')
        elif mv == (0,-1):
            world.move_kirk('UP')
 #           print('UP')
        elif mv == (1,0):
            world.move_kirk('RIGHT')
  #          print('RIGHT')
        elif mv == (-1,0):
            world.move_kirk('LEFT')
   #         print('LEFT')


def pathfinding_brut(start, carte, char):
    close_list = {}
    open_list = {}
    current_node = start
    open_list[current_node] = (0, start)
    h = len(carte)
    w = len(carte[0])

    is_found = False
    while not is_found:
#        for i,j in close_list.keys():
#            world.carte[j][i] = '*'
#        for i,j in open_list.keys():
#            world.carte[j][i] = 'o'
#        world.carte[current_node[1]][current_node[0]] = '0'
#        world.carte[world.kirk.pos[1]][world.kirk.pos[0]] == 'T'
#        for row in world.get_carte():
#            print(row)
        #input('')
#        time.sleep(0.005)


        last_parent = False
        for xn, yn in neighboor(*current_node, carte):
            open_list = update_open_list(*current_node, xn, yn, open_list, close_list)
            if carte[yn][xn] == char :
                last_parent = xn, yn
                close_list[(xn, yn)] = open_list[(xn, yn)]
                break

        close_list[current_node] = open_list[current_node]
        del open_list[current_node]

        if last_parent :
            break

        current_node = False
        for k, v in open_list.items():
            for i in range(1000):
                if v[0] == i:
                    current_node = k
                    break
            if current_node:
                break

    trace = get_trace(last_parent, close_list, start)
    return trace

def neighboor(x, y, carte):
    r = len(carte)
    c = len(carte[0])
    if y < r-1 and carte[y+1][x] != "#": # and carte[y+1][x] != "?":
        yield (x, y+1)
    if y > 0 and carte[y-1][x] != "#":# and carte[y-1][x] != "?":
        yield (x, y-1)
    if x < c-1 and carte[y][x+1] != "#":# and carte[y][x+1] != "?":
        yield (x+1, y)
    if x > 0 and carte[y][x-1] != '#':# and  carte[y+1][x-1] != "?":
        yield (x-1, y)

def update_open_list(x, y, xn, yn, open_list, close_list):
    score = open_list[(x,y)][0] + 1
    if (xn, yn) in close_list.keys():
        pass
    elif not (xn, yn) in open_list.keys():
        open_list[(xn, yn)] = (score, (x,y))
    else :
        if open_list[(xn, yn)][0] > score : # this path is better
            open_list[(xn, yn)] = (score, (x,y))
    return open_list

def pathfinding_astar(start, end, carte):

    close_list = {}
    open_list = {}
    current_node = start
    open_list[current_node] = (0,current_node)

    count = 0
    while True:


        #### tracé
        for i,j in close_list.keys():
            world.carte[j][i] = '*'
        for i,j in open_list.keys():
            world.carte[j][i] = 'o'
        world.carte[current_node[1]][current_node[0]] = '0'
        world.carte[world.kirk.pos[1]][world.kirk.pos[0]] == 'T'
        #for row in world.get_carte():
        for row in world.carte:
            print(''.join(row))
        #input('')
        time.sleep(0.07)
#        input('')

        count += 1
        if count > 5000:
            print(f'max iteration reached : {count}')

        x, y = current_node
        for xn, yn in neighboor(x, y, carte):
            if not carte[yn][xn] == '?':
                open_list = update_open_list(x, y, xn, yn, open_list, close_list)

        close_list[current_node] = open_list[current_node]
        del open_list[current_node]

        if end in open_list.keys():
            final_node =  {end : open_list[end]}
            last_parent = open_list[end][1]
            break

        current_node = get_next_node(open_list, end)
        if current_node == None: # there is no path to point
            return None

    print(f'========= iterations : {count} =================')
    trace = get_trace(last_parent, close_list, start)
    return trace

def get_trace(prev_node, close_list, start):
    trace = [prev_node]
    while True:

        prev_node = close_list[prev_node][1]
        trace += [prev_node]
        if prev_node == start:
            break
    return trace

def get_next_node(open_list, c_pos):

    best_node = None
    best_heuristic = 99999
    for k, v in open_list.items():
        score = v[0]
        #dist = abs(k[0] - c_pos[0]) + abs(k[1] - c_pos[1])*1.1
        dist = (((k[0] - c_pos[0])**2 + (k[1] - c_pos[1])**2)**0.5)*1.1
        heuristic = score + dist
        if heuristic < best_heuristic:
            best_heuristic = heuristic
            best_node = k
    return best_node


from world_map import Carte, Kirk, carte

#r, c, a = 10, 30, 200

kirk = Kirk(carte)
world = Carte(carte, kirk)
start_pos = kirk.pos


# game loop
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.

#OBdef kirk_talk(msg):
#
#    carte_temp = []
#    k_pos = kirk.pos
#    for row in world.get_carte():
#        carte_temp = []
#    for i,j in close_list.keys():
#        world.carte[j][i] = '*'
#    for i,j in open_list.keys():
#        world.carte[j][i] = 'o'
#    world.carte[current_node[1]][current_node[0]] = '0'
#    world.carte[world.kirk.pos[1]][world.kirk.pos[0]] == 'T'
#    for row in world.get_carte():
#        print(row)
#    #input('')
#    time.sleep(0.005)

#r, c, a = [int(i) for i in input().split()]
is_fini = False
while True:

    kr, kc = kirk.pos #[int(i) for i in input().split()]
    #kr, kc = [int(i) for i in input().split()]

    carte=[]
    for row in world.get_carte():
        carte += [row]
    #for i in range(r):
    #    row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
    #    carte += [row]

    start = (kr, kc)

    path = pathfinding_brut(start, carte, '?')

    for j in range(kc-2, kc+3):
        for i in range(kr-2, kr+3):
            if 0 < i < len(carte[0]) and 0 < j < len(carte):
                if carte[j][i] == 'C':
                    print('Nous avons trouvé la console!')
                    input('')
                    temp_path = pathfinding_astar((i,j), start,  carte)
                    if temp_path != None:
                        print('Nous pouvons l\'atteindre!')
                        input('')
                        path = temp_path
                        move(start, path)
                        print('objectif ateint, nous rentrons au point de rendez-vous')
                        path = pathfinding_astar((i,j), start_pos,  carte)
                        for i,j in path:
                            world.carte[j][i] = ' '
                        for row in world.carte:
                            print(''.join(row))
                        time.sleep(5)

                        move(start, path[::-1])
                        print('===================================')
                        print('===================================')
                        print('=====*****===*===*===**============')
                        print('=====*=======**==*===*==*==========')
                        print('=====***=====*=*=*===*===*=========')
                        print('=====*=======*==**===*==*==========')
                        print('=====*****===*===*===***===========')
                        print('===================================')
                        print('===================================')

                        is_fini = True
                        break
                    print('mais nous ne pouvons l\'atteindre:=!')
                    input('')
        if is_fini:
            break
    if is_fini:
        break

    path = path[-1:1:-1]#path[-1:-4:-1]
    move(start, path)


#print("Debug messages...", file=sys.stderr)
