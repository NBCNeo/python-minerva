import random
import numpy as np
import matplotlib.pyplot as plt

def hat_check(N):
    x = list(range(N))
    random.shuffle(x)
    #print(x)
    correct = 0
    for i in range(N):
        if x[i] == i:
            correct += 1
    return correct

def average_hat_check(N, samples):
    return np.mean([hat_check(N) for i in range(samples)])

X = list(range(1,50))
Y = [average_hat_check(x,1000) for x in X]

plt.plot(X,Y)
plt.show()
