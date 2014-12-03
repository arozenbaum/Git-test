#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Anna
#
# Created:     25/11/2014
# Copyright:   (c) Anna 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
from math import factorial

TRUE = 1
FALSE = 0

PRINTFOO = 1
PRINTDIAG = 1

ONSTATES = (1,2,3, 4)
VARNAMES = 1
LISTS = 2
ALL = 3
TEST1 = 4

##def nCk(n,k):
##    if n == 0 or k == 0:
##        return 0
##    if n < k or n < 0 or k < 0:
##        print "nCk rerror"
##        return -1
##    else:
##        return factorial(n)/(factorial(k)*factorial(n-k))



def print2(s, variables, onstate):
    if onstate in ONSTATES:
        if onstate == ALL:
            print "~"+s
        else:
            print "~"+s+"~"
        print variables
        print "\n"
    else:
        print "no"


def place_bombs(columns, rows, num_bombs):
    if PRINTFOO: print "\n ---in place_bombs---"
    bomb_columns = []
    bomb_rows = []
    bomb_placement = random.sample(range(columns*rows), num_bombs)
    print2("bomb_placement", bomb_placement, LISTS)

    for item in bomb_placement:
        bomb_columns.append(item%columns)
        bomb_rows.append(item/columns)

##    for r in range(num_bombs):
##        bomb_columns.append(random.randrange(columns))
##        bomb_rows.append(random.randrange(rows))
    print2 ("*",("bomb_columns" , bomb_columns, "bomb_rows", bomb_rows), VARNAMES)
    return bomb_columns, bomb_rows


def get_local(test_coord):
    mods = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    test_coords = []

    for r in range(len(mods)):
        test_coords.append(test_coord)

    zipper = zip(mods, test_coords)

    local_coords = []
    for p in zipper:
        pzip = zip(p[0],p[1])
        local_coords.append((sum(pzip[0]), sum(pzip[1])))

    print2("test_coord, local_coords", (test_coord, local_coords), LISTS)
    return local_coords

def count_bombs(test_coord, bombs):
    if PRINTFOO: print "in count_bombs()"

    local_coords = get_local(test_coord)
    count = 0
    for bomb in bombs:
        if bomb in local_coords:
            count+=1
            print2 ("bomb location:", bomb, 2)
    return count

def make_grid((columns, rows), num_bombs):
    if PRINTFOO: print "in make_grid. num columns, rows, bombs:", columns, rows, num_bombs
##    grid = [range(rows) for i in range(columns)]
    grid = [[{"bomb":FALSE, "clicked":FALSE} for r in range(rows)] for c in range(columns)]
##    for column in range(columns):
##        for row in range(rows):
##            grid[row, column] = {"bomb":0, "clicked":0}

    grid[0][1]['bomb'] = "yarp"

    bomb_locs = place_bombs(columns, rows, num_bombs)
    bomb_coords = zip(bomb_locs[0], bomb_locs[1])


    print2("count_bombs(1,1), bomb_coords", (count_bombs((1,1), bomb_coords)), TEST1)
    print2 ("bomb_coords",  bomb_coords, ALL)

    for b in bomb_coords:
        grid[b[0]][b[1]]['bomb'] = TRUE
        print b, grid[b[0]][b[1]]

    return grid

def print_grid(grid):
    for item in grid:
        print item




def main():

    print_grid(make_grid((5,3), 4))

if __name__ == '__main__':
    main()
