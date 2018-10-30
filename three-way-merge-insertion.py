import random
import time
import math
import matplotlib.pyplot as plt

def insertion_sort(l):
    for j in range(1, len(l)):
        k = l[j]
        i = 0
        while k > l[i] and i < j:
            i += 1
        l.insert(i, k)
        l.pop(j+1)


def merge3_insertion_sort(X,t): #t is the chosen threshold to apply insertion sort
    n = len(X)
    if n == 0 or n == 1:
        #CONQUER
        return X

    elif n <= t:
        insertion_sort(X)

    else:
        #DIVIDE

        if n%3 == 0:
            a = n/3
            b = 2*a

        else:
            a = int(n/3)
            b = 2*a+1

        L = merge3_insertion_sort(X[:a],t) + [float('inf')]
        M = merge3_insertion_sort(X[a:b],t) + [float('inf')]
        R = merge3_insertion_sort(X[b:],t) + [float('inf')]

        #COMBINE

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

for d in range(100,1000):
    Xcor.append(d)
    l = [random.randint(-d,d) for i in range(d)]
    start = time.time()
    merge3_insertion_sort(l,100)
    end = time.time()
    Ycor.append(end-start)

plt.plot(Xcor,Ycor,'r',Xcor,[(x*math.log(x/100,2)+x*100)/10000000 for x in Xcor],'b-')
plt.show()
