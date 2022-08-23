#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Nidhi Vraj Sadhuvala, nsadhuva
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):

    #successor_list has all the successor states of each pichu
    successor_list=[add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]
    
    #final_successors_list returns the final map(goal after placing k pichus) only if it satisfies the condition in check_valid function
    final_successors_list = [x for x in successor_list if check_valid(x)]
    return final_successors_list

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

#to check the validity of the placement of pichu in the given map
def check_valid(house_map):
    pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"]
    
    for loc in pichu_loc: #to check for each pichu in the map
        r,c=loc
    
   #traversing upwards in a row from pichu_loc to check if there's another pichu located upwards facing each other
        for i in range(r-1,-1,-1):
            
            if (house_map[i][c]) == "p":
                return False

            #if 2 pichus are not seeing each other but encounters a wall "X" or "@" then this condition is valid 
            if (house_map[i][c] in ["X","@"]):
                break

    #traversing downwards in a row from pichu_loc to check if 2 pichus are seeing each other 
        for i in range(r+1,len(house_map)):
            if (house_map[i][c]) == "p":
                return False
                
            if (house_map[i][c] in ["X","@"]):
                break

    #traversing right in a column from pichu_loc to check if 2 pichus are seeing each other
        for i in range(c+1,len(house_map[0])):
            if (house_map[r][i]) == "p":
                return False
                
            if (house_map[r][i] in ["X","@"]):
                break
            
    #traversing left in a column from pichu_loc to check if 2 pichus are seeing each other
        for i in range(c-1,-1,-1):
            if (house_map[r][i]) == "p":
                return False
                
            if (house_map[r][i] in ["X","@"]):
                break

        r,c=loc
    #traversing diagonally upper right from pichu_loc to check if 2 pichus are seeing each other
        while(r>=0 and c<len(house_map[0])-1):
            r=r-1
            c=c+1

            #condition to make sure that the traversal in (row,col) index pair is inside the map
            if r <0 or c > len(house_map[0])-1:
                break
            if(house_map[r][c]=="p"):
                return False
                
            if(house_map[r][c] in ["X","@"]):
                break
        r,c=loc
        
    #traversing diagonally down right from pichu_loc to check if 2 pichus are seeing each other
        while(r<len(house_map)-1 and c<len(house_map[0])-1):
            r=r+1
            c=c+1
            if r > (len(house_map))-1 or c>len(house_map[0])-1:
                break
            if(house_map[r][c]=="p"):
                return False
                
            if(house_map[r][c] in ["X","@"]):
                break
 
        r,c=loc
    #traversing diagonally upper left from pichu_loc to check if 2 pichus are seeing each other
        while(r>=0 and c>=0):
            r=r-1
            c=c-1
            if r < 0 or c < 0:
                break
            if(house_map[r][c]=="p"):
                return False
                
            if(house_map[r][c] in ["X","@"]):
                break
        r,c=loc
    #traversing diagonally down left from pichu_loc if 2 pichus are seeing each other
        while(r<len(house_map)-1 and c>=0):
            r=r+1
            c=c-1
            if c < 0 or r > len(house_map)-1:
                break
            if(house_map[r][c]=="p"):
                return False
                
            if(house_map[r][c] in ["X","@"]):
                break

    return True
   
# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]

    #visited has all the maps that have been explored 
    visited=[]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            #if the current map in successors has not been explored then it appends to the visited list and also appends it to the fringe
            if new_house_map not in visited:
                visited.append(new_house_map)
                fringe.append(new_house_map)
    return ("",False)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")