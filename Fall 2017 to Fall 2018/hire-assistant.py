import random
import matplotlib.pyplot as plt
import numpy as np
import math

def hire_assistant(numofdays):
    hires = 0
    start = random.random()
    current = start
    for day in range(numofdays):
        applicant = random.random()
        if applicant > current:
            hires+=1
            current = applicant

    return hires

def simulation1(repetitions,hired,num_of_days):
    favorable_events = 0
    for i in range(repetitions):
        #print(hire_assistant(num_of_days))
        if hire_assistant(num_of_days) == hired:
            favorable_events+=1

    return float(favorable_events)/float(repetitions)

#print(simulation1(100,1,100))

X = [n for n in range(1,2001)]
Y = [np.mean([hire_assistant(d) for s in range(50)]) for d in X]

plt.plot(X,Y, color = "red")
plt.plot(X,[math.log(x) for x in X])
plt.show()


print(hire_assistant(10000))
