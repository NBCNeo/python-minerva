import random
import time
import math
import matplotlib.pyplot as plt

def merge_sort3(X):
    n = len(X)
    if n == 0 or n == 1:
        #conquer
        return X

    else:
        #divide
        if n%3 == 0:
            a = n/3
            b = 2*a
        else:
            a = int(n/3)
            b = 2*a+1
        L = merge_sort3(X[:a]) +[float('inf')]
        M = merge_sort3(X[a:b]) + [float('inf')]
        R = merge_sort3(X[b:]) +[float('inf')]

        #combine
        for i in range(n):
            X[i] = min(L[0],M[0],R[0])
            if X[i] == L[0]:
                L = L[1:]
            elif X[i] == M[0]:
                M = M[1:]
            else:
                R = R[1:]

        return X

Xcor = []
Ycor = []

for d in range(1,1000):
    Xcor.append(d)
    l = [random.randint(-d,d) for i in range(d)]
    start = time.time()
    merge_sort3(l)
    end = time.time()
    Ycor.append(end-start)

plt.plot(Xcor,Ycor,'r',Xcor,[x*math.log(x,3)/1000000 for x in Xcor],'b-')
plt.show()
