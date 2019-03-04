import random
import time
import math
import matplotlib.pyplot as plt

def merge_sort2(X):
    steps = 0
    n = len(X)
    if n == 0 or n == 1:
        #conquer
        return X
    else:
        #divide

        m = int(n/2) #midpoint: index for the first term of right half
        L = merge_sort2(X[:m]) +[float('inf')]
        R = merge_sort2(X[m:]) +[float('inf')]

        #combine
        for i in range(n):
            X[i] = min(L[0],R[0])
            if X[i] == L[0]:
                L = L[1:]
            else:
                R = R[1:]

        return X

#m = 50000
#test = [random.randint(-1000,1000) for i in range(m)]

Xcor = []
Ycor = []

for d in range(1,1000):
    Xcor.append(d)
    l = [random.randint(-d,d) for i in range(d)]
    start = time.time()
    merge_sort2(l)
    end = time.time()
    Ycor.append(end-start)

plt.plot(Xcor,Ycor,'r',Xcor,[x*math.log(x,2)/900000 for x in Xcor],'b-')
plt.show()
