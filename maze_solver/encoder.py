import argparse
import numpy as np

# Running command
# python3 encoder.py --grid gridfile > mdpfile
# python3 encoder.py --grid data/maze/grid10.txt > mdp10.txt

parser = argparse.ArgumentParser(description='MAZE TO MDP ENCODER')
parser.add_argument('--grid', type=str, help='Path to the input Maze Grid file')
args = parser.parse_args()

maze_grid = args.grid

maze = list(list())

with open(maze_grid, 'r') as f:
    for line in f:
        maze.append(list(map(int,line.split())))

numStates = int()
numActions = int()
start = int()
end = []
mdptype = "episodic"
gamma = 0.9

actions = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}

# for i in maze:
#     for j in range(len(i)):
#         if j == len(i) - 1:
#             print(i[j], end="")
#         else:
#             print(i[j], end=" ")
#     print("\n", end="")


valid_state = 0
n = len(maze)
m = len(maze[0])
states = - np.ones((n, n), int)

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            start = valid_state
        elif maze[i][j] == 3:
            end.append(valid_state)
        if maze[i][j] != 1:
            states[i][j] = valid_state
            valid_state += 1
#print(states)
transitions = []
p = [1,1,1,1]
reward = n*m*10
normie_reward = -2
for i in range(1,n-1):
    for j in range(1,m-1):
        s1 = states[i][j]
        if s1 == -1:
            continue
        s2 = []
        r = []
        t = []
            
        # North
        if states[i-1][j] != -1:
            s2.append(states[i-1][j])
            if maze[i-1][j] == 3:
                r.append(reward)
            else:
                r.append(normie_reward)
        else:
            s2.append(states[i][j])
            r.append(-reward)
        # South
        if states[i+1][j] != -1:
            s2.append(states[i+1][j])
            if maze[i+1][j] == 3:
                r.append(reward)
            else:
                r.append(normie_reward)
        else:
            s2.append(states[i][j])
            r.append(-reward)
        # East
        if states[i][j+1] != -1:
            s2.append(states[i][j+1])
            if maze[i][j+1] == 3:
                r.append(reward)
            else:
                r.append(normie_reward)
        else:
            s2.append(states[i][j])
            r.append(-reward)
        # West
        if states[i][j-1] != -1:
            s2.append(states[i][j-1])
            if maze[i][j-1] == 3:
                r.append(reward)
            else:
                r.append(normie_reward)
        else:
            s2.append(states[i][j])
            r.append(-reward)


        for k in range(4):
            t.append("transition " + str(s1) + " " + str(k) + " " + str(s2[k]) + " " + str(r[k]) + " " + str(p[k]))
        transitions += t

print("numStates", valid_state)
print("numActions", 4)
print("start", start)
print("end", end=" ")
for i in end:
    print(i, end=" ")
print("\n", end="")
for i in transitions:
    print(i)
print("mdptype", mdptype)
print("discount",  gamma)
