import numpy as np
import subprocess
import os

for i in range(5):
    n = np.random.randint(100)
    init = np.random.randint(n)
    final = np.random.randint(n)
    t = np.random.randint(100)
    file = 'input/input' + str(i) + '.txt'
    with open(file, 'w') as fp:
        fp.write(str(n))
        fp.write('\n')
        fp.write(str(init))
        fp.write('\n')
        fp.write(str(final))
        fp.write('\n')
        fp.write(str(t))
        fp.write('\n')
        for j in range(n):
            prob = np.random.dirichlet(np.ones(n),size=1)
            for k in prob:
                for m in k:
                    fp.write(str(m))
                    fp.write(' ')
            fp.write('\n')

    data, temp = os.pipe()
    os.write(temp, bytes("5 10\n", "utf-8"));
    os.close(temp)
    s1 = subprocess.check_output("python3 markov_chain.py < input/input" + str(i) + ".txt > output/output" + str(i) + ".txt", stdin = data, shell = True)
    s2 = subprocess.check_output("python3 markov_chain_DP.py < input/input" + str(i) + ".txt > output/output_DP" + str(i) + ".txt", stdin = data, shell = True)