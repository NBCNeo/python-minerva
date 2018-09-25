def max_subarray(x):
    n = len(x)
    sums = []
    for i in range(n-1):
        for j in range(i+1,n):
            sums.append(sum(x[i:j]))
    return max(sums)

def incremental_max_subarray1(x,mx): #given the sum
    n = len(x)
    s = x[-1]
    maxsum = s
    for i in range(2,n+1):
        s += x[-i]
        if s > maxsum:
            maxsum = s
    return max(mx,maxsum)


def incremental_max_subarray2(x,mx): #given the indexes
    n = len(x)
    s = x[-1]
    maxsum = s
    j = -1
    for i in range(2,n+1):
        s += x[-i]
        if s > maxsum:
            maxsum = s
            j = -i
    if maxsum > mx[2]:
        return (n+j,n,maxsum)
    else:
        return mx

example = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
example2 = [20,-16,-23,18,20]

def recursive_max_subarray1(x):
    n = len(x)
    if n == 1:
        return x[0]
    else:
        return incremental_max_subarray1(x,recursive_max_subarray1(x[:-1]))

#print(max_subarray(example[:-6]))
#print(incremental_max_subarray1(example[:-5],38))
#print(incremental_max_subarray2(example[:-5],(7,9,38)))
print(recursive_max_subarray1(example))
