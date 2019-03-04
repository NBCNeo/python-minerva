import random
import math

def worst_sort(X):
    num_of loops = 0
    n = len(X)
    Y = X[:]
    Y.sort()
    while X != Y:
        random.shuffle(X)
        num_of_loops += 1
    return num_of_loops

#best case complexity: O(1)
#average case complexity: log_a(1/2) with a = (n!-1)/n!
#worst case complexity: log_a(0.99) or infinity?

def median_finder(X,d):
    lower_percentile = 0.5-d/2
    upper_percentile = 0.5+d/2
    Y = X[:]
    Y.sort()
    n = len(Y)
    low_k = math.ceil(n*lower_percentile)
    big_k = math.floor(n*upper_percentile)
    median_low = Y[low_k-1]
    median_high = Y[big_k+1]
    my_try = random.choice(X)
    retry = True
    while my_try < median_low and my_try > median_high and retry:
        my_try = random.choice(X)
        r = random.random()
        if r > 0.9:
            retry = False
    return my_try if my_try < median_low and my_try else False

#average case complexity:
