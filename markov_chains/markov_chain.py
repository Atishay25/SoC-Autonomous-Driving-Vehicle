import numpy as np

def multiply(A,B,n):
    C = np.zeros((n,n), float)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


n = int(input())    # number of states
initial_state = int(input())
final_state = int(input())
t = int(input())
m = list()

for i in range(n):
    l = list(map(float, input().split()))
    m = m + l

p = np.array(m).reshape(n,n)

P_t = np.zeros((n,n), float)
t1 = t

for i in range(n):
    P_t[i][i] = 1

while(t > 0):
    if t%2 != 0:
        P_t = multiply(P_t, p, n)
    p = multiply(p,p,n)
    t = t // 2
    #P_t = multiply(P_t,p,n)
    #t -= 1

prob = P_t[initial_state][final_state]

# ans = "Probability of reaching state " + str(final_state) + " at time t = " + str(t1) + " starting from state " + str(initial_state) + " at t = 0 is : "
# print(ans, prob)
print(prob)