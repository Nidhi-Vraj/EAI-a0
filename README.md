# Part 1: Navigation

## Route pichu:
The aim is to find the shortest path from agent “p” to my location “a”. The code was going into infinite loop as it was flickering between two coordinates. So I have used the below algorithm to fix this issue.

## Search Abstraction:

### State Space/ Valid States:
To find all successive states which are reachable from an instance. In other words, to be able to check whether a state is valid or not. Hence, in this problem the state space would be all the posiitons that the pichu can move to which is to move in the direction of dots ".". The pichu has to find another path if it encounters an "X" which is a wall and so it cannot pass through. 

### Initial State:
Start position where "p" is located.

### Successor Function:
Finding next possible moves which are valid from the current pichu's location. A state is only valid if there is no obstacle/wall "X" when traversing throught the path. In this algorithm, next move is considered based on the heuristic value. I'm calculating heuristic value for each state to know which state I can traverse so that I can get the optimal path. The shorter the value, the most optimal is the path.

### Goal State:
Goal state is when we find the shortest path from "p" to "@". Hence, when we encounter "@" while traversing through the grid that's when we reach the goal state.

### Cost function:
Heuristic function "f(s) = g(s) + h(s)" calculates the cost to reach the goal position.  

* I have implemented A* algorithm in particular to solve this problem. The searches will be done more efficiently than compared to BFS or DFS because this search algorithm will prioritize the states that are much more likely to be closer to the goal state than the other states. Hence, the better the estimate the more efficient the search.
    A* uses:
        * Admissible Heuristic Function,
        * Right evaluation function,
        * Best First search 

### Evaluation Function:
        f(s) = g(s) + h(s)
        where, g(s) = calculates cost from initial state to current state by using Manhattan Distance formula
               h(s) is Admissible = calculates Manhattan distance from the current position to goal position 
                                  = |Xn - Xg| + |Yn - Yg|
                              where, Xn- row coordinate of current state
                                     Xg- row coordinate of goal state
                                     Yn- col coordinate of current state
                                     Yg- col coordinate of goal state

* My Heuristic is consistent so I have used Manhattan Distance. My pichu can either travel in Upper, Downward, Left and Right directions so my heuristic is admissible and consistent. So, thats why I dont have to revisit the nodes again which makes my algorithm more efficient.

## Fringe:
All the valid states are appended to the fringe calculating the distance alongside as I traverse through. Fringe stores the heuristic function for each move. I'm sorting this fringe by heuristic values in ascending order so I can pop the first element and assigning that state to my current move which is then being checked if it has reached the goal. This way, I get the optimal solution as I'm tracking the path based on lower heuristic values.

## Difficulties Faced:
* Initially, the code was taking a lot of time to execute and repeated states were being shown in the fringe so I have declared a "visited" state which stores all the states that are explored to make the algorithm more efficient. So, the next time I traverse through the map for a given instance, I will not explore the state that has already been visited so instead the next possible move will be appended to the fringe.

* While calculating the cost for heuristic function, I have encountered a problem in g(s). My g(s) function was the distance as I traverse from the initial position to the current position but I was not able to get the optimal solution because a state whose cost was more than the other state was considered because it was the first element in the fringe to be popped. But, later I changed the cost function to manhattan distance from initial position to current position and then I was able to get the shortest path.

* Another problem I faced is when I couldn't display -1 as path if there's no solution found for a given test case. Because my solution is returning a tuple which contains distance traversed, and a string that displays the path. So, I was getting an error because -1 is integer type. So I had to add an if-else statement to make sure that if there's a path found it will return a tuple disaplying the solution otherwise it simply displays -1.


# Part 2: Hide-and-Seek

## Arrange_Pichus
The aim is to arrange k pichus such that no two pichus see other from any direction but a wall "X" or "@" can obscure the view between pichus. I have solved this problem using Depth First Search algorithm.

## Search Abstraction:

### State Space:
The total number of possibilities to place k pichus on the map in valid positions. Given the condition that no two pichus can see other in either upward, downward, left, right and all the 4 diagonal directions. So, pichus can only be placed if there's a dot "." checking the validity of each pichu.
Hence, the state space would be to place all the k pichus after "X" or "@" or between these walls such that they can obscure the view between any pichus. 

### Initial State:
Initial state here is the initial house map that contains a pichu at a given instance. 

### Goal State:
Goal state is when we arrange all the k pichus in the house_map such that there are no conflicts and satisfies all the given conditions for every pichu in the map.

* If there's no solution found for a given test case, then the ouput returns False.

### Successor Function:
My successor function is a list of all possible successors for a given instance of a map. For example, if my initial house_map has one pichu placed at a given location, the successor state would give a map in which a next pichu will be placed wherever there's a dot ".". It will give all possible successors for that particular initial house_map and so on. I am storing all these successors for each house_map in a list called "successors_list". And then I'm checking the validity of each successor list genearted by a house_map by checking if no pichu is seeing other. If there are two pichus seeing each other in either of all 8 directions, then I'm not considering that house map. I am then passing all the valid maps into the fringe. This process repeats until I find a map which satisfies all the conditions in check_valid function and this map is returned in my final_successors_list.   

### Cost Function:
No cost function is implemented in this algorithm.
        
### Visited:
I have used a visited state to store all the new house maps that are explored in order to reduce the time and space complexity such that no house map that has already been visited will be appended to the fringe again and again.



