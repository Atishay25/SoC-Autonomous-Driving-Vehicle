import argparse
import numpy as np

# Running command
# python3 planner.py --mdp data/mdp/continuing-mdp-2-2.txt --algorithm vi

def print_data():
    print("numStates", numStates)
    print("numActions", numActions)
    print("start", start)
    print("end", end)
    print("T", T)
    print("R", R)
    print("mdptype", mdptype)
    print("discount", gamma)

def value_iteration(numStates, numActions, T, R, gamma):
    V = np.zeros(numStates, float)
    theta = 1e-12
    k = 1
    while 1:
        d = 0
        for s in range(numStates):
            v = V[s]
            val = 0
            for j in range(numActions):
                summ = 0
                for k in range(numStates):
                    summ += T[s][k][j] * (R[s][k][j] + (gamma * V[k]))
                if val < summ:
                    val = summ
            V[s] = val
            d = max(d, abs(v-V[s]))
        if d < theta:
            break
    policy = np.zeros(numStates, dtype=int)
    for s in range(numStates):
        val = 0
        for j in range(numActions):
            summ = 0
            for k in range(numStates):
                summ += T[s][k][j] * (R[s][k][j] + gamma * V[k])
            if summ > val:
                val = summ
                policy[s] = j
    return V, policy

parser = argparse.ArgumentParser(description='MDP Planner')
parser.add_argument('--mdp', type=str, help='Path to the input MDP file')
parser.add_argument('--algorithm', choices=['vi', 'hpi', 'lp'], help='Algorithm: vi, hpi, or lp')

args = parser.parse_args()

mdp_file = args.mdp

algo = args.algorithm

start = int()
end = []
numStates = int()
numActions = int()
mdptype = str()
gamma = float()
T = None
R = None

with open(mdp_file, 'r') as fp:
    for line in fp:
        d = line.split()
        if d[0] == "numStates":
            numStates = int(d[1])
        elif d[0] == "numActions":
            numActions = int(d[1])
        elif d[0] == "start":
            start = int(d[1])
            T = np.zeros((numStates, numStates, numActions), float)
            R = np.zeros((numStates, numStates, numActions), float)
        elif d[0] == "end":
            end = list(map(int, d[1:]))
        elif d[0] == "mdptype":
            mdptype = d[1]
        elif d[0] == "discount":
            gamma = float(d[1])
        else:
            T[int(d[1])][int(d[3])][int(d[2])] = float(d[5])
            R[int(d[1])][int(d[3])][int(d[2])] = float(d[4])


#print_data()

V, pi = np.zeros(numStates), np.zeros(numStates)

if algo == 'vi':
    V, pi = value_iteration(numStates, numActions, T, R, gamma)

elif algo == 'hpi':
    print("Running Howard's Policy Iteration algorithm...")

elif algo == 'lp':
    print('Running Linear Programming algorithm...')

else:
    print('Invalid algorithm specified. Please choose either vi, hpi, or lp.')

for j in range(numStates):
    print(V[j], pi[j])