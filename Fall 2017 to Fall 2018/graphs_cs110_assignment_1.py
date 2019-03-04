import math
import matplotlib.pyplot as plt

x = [i for i in range(1,200)]

y1 = [a*math.log(a,2) for a in x]
y2 = [a*math.log(a,3) for a in x]
m=10
y3 = [a*math.log(a/m,3)+a*m if a/m >= 1 else m**2 for a in x]

plt.plot(x,y1,'r-',x,y2,'b-',x,y3,'g-')
plt.show()
