import numpy as np

n = int(input())    # number of states
initial_state = int(input())
final_state = int(input())
T = int(input())
M = list()

for i in range(n):
    l = list(map(float, input().split()))
    M = M + l

matrix = np.array(M).reshape(n,n)

print(matrix)