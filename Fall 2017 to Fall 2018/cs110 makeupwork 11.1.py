import matplotlib.pyplot as plt
import timeit

def cut_rod(p,n):
    if n==0:
        return 0
    q = -float("inf")
    for i in range(n):
        q = max(q,p[i]+cut_rod(p,n-i-1))
    return q

def extended_bottom_up_cut_rod(p,n):
    r = list(range(n+1))
    s = list(range(n+1))
    for j in range(1,n+1):
        q = -float('inf')
        for i in range(1,j+1):
            if q < p[i] + r[j-i]:
                q=p[i]+r[j-i]
                s[j]=i
        r[j]=q
    return [r,s]

def print_cut_rod_solution(p,n):
    s = extended_bottom_up_cut_rod(p,n)[1]
    while n>0:
        print(s[n])
        n = n - s[n]

p = [1,5,8,9,10,17,17,20,24,30,32,36,36,38]
p2 = [0,1,5,8,9,10,17,17,20,24,30,32,36,36,38]

times = []
dynamic = []

for j in range(15):
    start = timeit.default_timer()
    cut_rod(p,j)
    stop = timeit.default_timer()
    times.append(stop - start)
    start2 = timeit.default_timer()
    print_cut_rod_solution(p2,j)
    stop2 = timeit.default_timer()
    dynamic.append(stop2 - start2)

sum=0
nsums = 1000000
for z in range(nsums):
    start = timeit.default_timer()
    cut_rod(p,1)
    stop = timeit.default_timer()
    sum += stop - start

y = [0 for x in range(15)]
y[0] = times[0]
y[1] = sum/nsums

for a in range(2,15):
    y[a] = y[0]*2**(a-1)
plt.plot(list(range(15)),times)
plt.plot(list(range(15)),y,color ='red')
plt.plot(list(range(15)),dynamic, color='green')
plt.show()




print_cut_rod_solution(p2,10)
print(y[1])
