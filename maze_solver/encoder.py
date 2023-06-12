import argparse

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
        maze.append(map(int,line.split()))

# for i in maze:
#     for j in range(len(i)):
#         if j == len(i) - 1:
#             print(i[j], end="")
#         else:
#             print(i[j], end=" ")
#     print("\n", end="")

for row in maze:
    for i in row:
        if i == 2:
            print(4)