import argparse
import numpy as np

# Running command
# python3 decoder.py --grid gridfile --value_policy value_and_policy_file
# python3 decoder.py --grid data/maze/grid10.txt --value_policy value_and_policy_file

parser = argparse.ArgumentParser(description='DECODER')
parser.add_argument('--grid', type=str, help='Path to the input Maze Grid file')
parser.add_argument('--value_policy', type=str, help='Value and Policy file (i.e. output of planner.py)')
args = parser.parse_args()

maze_grid = args.grid
value_policy = args.value_policy

maze = list(list())

with open(maze_grid, 'r') as f:
    for line in f:
        maze.append(list(map(int,line.split())))

actions = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}

valid_state = 0
n = len(maze)
m = len(maze[0])
states = - np.ones((n, m), int)
start = int()
end = []
indices = dict()

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            start = valid_state
        elif maze[i][j] == 3:
            end.append(valid_state)
        if maze[i][j] != 1:
            states[i][j] = valid_state
            indices[valid_state] = [i,j]
            valid_state += 1

policy = []
with open(value_policy, 'r') as f:
    for line in f:
        policy.append(int(line.split()[-1]))

s = start
soln = ""

while s not in end:
    soln += actions[policy[s]] + " "
    a =  policy[s]
    if s == -1:
        print(soln)
        break
    i = indices[s][0]
    j = indices[s][1]
    if states[i][j] != s:
        print("Error")
        break
    if a == 0:
        s = states[i-1, j]
    elif a == 1:
        s = states[i+1, j]
    elif a == 2:
        s = states[i, j+1]
    else:
        s = states[i, j-1]

print(soln)