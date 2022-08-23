#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Nidhi Vraj Sadhuvala, nsadhuva
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
#Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]


# tracking the path from pichu's location "p" to goal "a" and so I am appending each move to the path which is returned as a string 
def track_path(move,curr_move):
        path=""

        #condition for traversing upwards
        if(move[0]-curr_move[0]==-1): 
                path='U'
        #condition for traversing downwards
        elif(move[0]-curr_move[0]==1): 
                path='D'
        #condition for traversing towards right
        elif(move[1]-curr_move[1]==1):
                path='R'
        #condition for traversing towards left
        elif(move[1]-curr_move[1]==-1):
                path='L'
        return path 

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        
        # Find goal position
        goal_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="@"][0]
        
        # Fringe has pichu's location, distance traversed by pichu, heuristic function value which gives the shortest and optimal path, 
        #     and the 4th parameter returns a string which has the path from initial state to the goal location
        fringe=[(pichu_loc,0,0,"")]
        
        # visited stores all the moves that have already been explored 
        visited=[pichu_loc]
        path=""
        
        while fringe:
                #sorting the fringe by heuristic function(3rd parameter) so that the states with lowest priority(low heuristic value) comes out first from the fringe because it gives the optimal path
                fringe.sort(key=lambda x:x[2])
                #the above sort method has been taken as a reference from the site for the syntax: "https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/"

                (curr_move,curr_dist,f_of_s,path)=fringe.pop(0)
                for move in moves(house_map, *curr_move):

                        #Manhattan distance from pichu's location(starting posiiton) to next possible move from current position
                        g_of_s = abs(move[0]-pichu_loc[0]+abs(move[1]-pichu_loc[1])) 

                        #Manhattan distance from goal location to the next possible move from current position
                        h_of_s = abs(move[0]-goal_loc[0]+abs(move[1]-goal_loc[1])) 

                        #calculating heuristic function because it gives the most promising states for calculating the optimal path
                        f_of_s = g_of_s + h_of_s

                        if house_map[move[0]][move[1]]=="@":
                                return (curr_dist+1,path+track_path(move,curr_move))

                        else:
                                if move not in visited:
                                        visited.append(curr_move)
                                        #fringe keeps track of the shortest path based on the value calculated by heuristic function
                                        fringe.append((move, curr_dist + 1,f_of_s,path+track_path(move,curr_move)))

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        solution = search(house_map)

        # solution returns a tuple containing distance from pichu to goal location and the directions that it has to follow
        if type(solution) == tuple:
        # the above syntax to check if a variable is tuple has been taken as a reference from the site "stackoverflow"
                print("Shhhh... quiet while I navigate!")
                print("Here's the solution I found:")
                print(str(solution[0]) + " " + solution[1])
        else:
                #if there's no solution found then it returns -1 as path length 
                print(-1) 


                        