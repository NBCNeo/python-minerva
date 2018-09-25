def max_sub(x):
    n = len(x)
    diffs = [x[i+1]-x[i] for i in range(n-1)]
    subarrays = []
    for length in range(1,n):
        subarrays += [sum(diffs[j:j+length]) for j in range(0,n-length)]
    return max(subarrays)

print(max_sub([100,113,110,85,105,102,86,63,81,101,94,106,101,79,94,90,97]))
