from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import numpy as np

def mc_pi(n):
    s = 0
    for i in range(n):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if (x**2 + y**2) < 1:
            s += 1
    return 4*s/n

# with ProcessPoolExecutor() as pool:
#     res = pool.map(mc_pi, [int(1e6) for i in range(5)])
with ProcessPoolExecutor(max_workers=4) as pool:
    res = pool.map(mc_pi, [int(1e6) for i in range(int(1e4))], chunksize=100)

# https://people.duke.edu/~ccc14/sta-663-2016/19B_Threads_Processses_Concurrency.html
print(np.array(list(res)))