import numpy as np

def findProbability(G, N, F, S, T):
 
    # Declaring the DP table
    P = [[0 for i in range(T + 1)]
            for j in range(N + 1)]
    # Probability of being at S
    # at t = 0 is 1.0
    P[S][0] = 1.0
  
    # Filling the DP table
    # in bottom-up manner
    for i in range(1, T + 1):
        for j in range(1, N + 1):
            for k in G[j]:
                P[j][i] += k[1] * P[k[0]][i - 1];
    print(P)
    return P[F][T]
 
# Driver code
if __name__=='__main__':
 
    # Adjacency list
    G = [0 for i in range(7)]
  
    # Building the graph
    # The edges have been stored in the row
    # corresponding to their end-point
    G[1] = [ [ 2, 0.09 ] ]
    G[2] = [ [ 1, 0.23 ], [ 6, 0.62 ] ]
    G[3] = [ [ 2, 0.06 ] ]
    G[4] = [ [ 1, 0.77 ], [ 3, 0.63 ] ]
    G[5] = [ [ 4, 0.65 ], [ 6, 0.38 ] ]
    G[6] = [ [ 2, 0.85 ], [ 3, 0.37 ],
             [ 4, 0.35 ], [ 5, 1.0 ] ]

    # N is the number of states
    N = 6
  
    S = 4
    F = 2
    T = 1
     
    print("The probability of reaching {} at "
          "time {}\nafter starting from {} is {}".format(
          F, T, S, findProbability(G, N, F, S, T)))
  
# This code is contributed by rutvik_56