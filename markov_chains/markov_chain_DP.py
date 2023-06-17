import numpy as np

n = int(input())    # number of states
initial_state = int(input())
final_state = int(input())
t = int(input())
m = list()


for i in range(n):
    l = list(map(float, input().split()))
    m = m + l

p = np.array(m).reshape(n,n)
p = np.transpose(p)

dp = np.zeros((n, t+1), float)

dp[initial_state][0] = 1

for i in range(1,t+1):
    for j in range(n):
        for k in range(n):
            dp[j][i] += p[j][k] * dp[k][i-1]

print(dp[final_state][t]) 
