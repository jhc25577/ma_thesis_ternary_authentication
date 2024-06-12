import random
import numpy as np

random.seed(42)
b = 512*512
for i in range(0, 10):
    with open(f"data_{i}.txt", "w") as f:
        a = list(np.random.randint(low = 3,size=b))
        s = ''.join(str(x) for x in a)
        f.write(s)
    