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


PRINTFOO = 1
PRINTDIAG = 1

ONSTATES = (1,3, 4, 5)
VARNAMES = 1
LISTS = 2
ALL = 3
TEST1 = 4
LINES = 5

##def nCk(n,k):
##    if n == 0 or k == 0:
##        return 0
##    if n < k or n < 0 or k < 0:
##        print "nCk rerror"
##        return -1
##    else:
##        return factorial(n)/(factorial(k)*factorial(n-k))

def print3(onstate, *args):
    if onstate in ONSTATES:
        for arg in args:
            print arg

def print2(s, variables, onstate):
    if onstate in ONSTATES:
        if onstate == ALL:
            print "~"+s
        else:
            print "~"+s+"~"
        print variables
        print "\n"


def place_bombs(rows, columns, num_bombs):
    if PRINTFOO: print "\n ---in place_bombs---"
    bomb_rows = []
    bomb_columns = []
    bomb_placement = random.sample(range(rows*columns), num_bombs)
    print2("bomb_placement", bomb_placement, LISTS)

    for item in bomb_placement:
        bomb_rows.append(item%rows)
        bomb_columns.append(item/rows)

##    for r in range(num_bombs):
##        bomb_rows.append(random.randrange(rows))
##        bomb_columns.append(random.randrange(columns))
    print2 ("*",("bomb_rows" , bomb_rows, "bomb_columns", bomb_columns), VARNAMES)
    return bomb_rows, bomb_columns


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

def make_grid((rows, columns), num_bombs):
    if PRINTFOO: print "in make_grid. num rows, columns, bombs:", rows, columns, num_bombs
##    grid = [range(columns) for i in range(rows)]
    grid = [[{"bomb":False, "clicked":False, "flagged":False} for r in range(columns)] for c in range(rows)]
##    for column in range(rows):
##        for row in range(columns):
##            grid[row, column] = {"bomb":0, "clicked":0}

#    grid[0][1]['bomb'] = "yarp"

    bomb_locs = place_bombs(rows, columns, num_bombs)
    bomb_coords = zip(bomb_locs[0], bomb_locs[1])


    print2("count_bombs(1,1), bomb_coords", (count_bombs((1,1), bomb_coords)), TEST1)
    print2 ("bomb_coords",  bomb_coords, ALL)

    for b in bomb_coords:
        grid[b[0]][b[1]]['bomb'] = True
        print b, grid[b[0]][b[1]]

    
	for r in range(rows):
		for c in range(columns):			
			grid[r][c]['number'] = count_bombs((r,c), bomb_coords) 
			print "square", r, c, grid[r][c]['number']

	return grid	
	
def print_grid(grid):
    string_list = [""]
    for idx, val in enumerate(grid):
        string_list[0]+=str(idx)
        print "stringlist[0]", string_list[0]
        print idx
    for row in grid:
        print2("",row, LISTS)
        tempstring = ""
        for column in row:
            tempstring+="]["
        string_list.append("["+tempstring+"]")


        for idx, val in enumerate(row):
               print "column number", idx, val

        print3(LINES, ".........")

    print [a for a, b in enumerate(grid)]

    for string in string_list:
        print "string" , string

def main():

    print_grid(make_grid((5,3), 4))

if __name__ == '__main__':
    main()
