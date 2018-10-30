def quicksort_partition(X):
    #print("Quicksort for X = ", X)
    n = len(X)
    x = X[-1]
    i = -1
    for j in range(n-1):
        if X[j] <= x:
            i+=1
            xj = X[j]
            X[j] = X[i]
            X[i] = xj
    #print("Pre-finished quicksort and X = ",X)
    xi1 = X[i+1]
    X[i+1] = X[-1]
    X[-1] = xi1
    #print("Finished quicksort and now X = ", X)
    return i+1

def quicksort_easy(X):
    if len(X) <= 1:
        return X
    else:
        partition = quicksort_partition(X)
        A = X[:partition]
        B = X[partition]
        C = X[partition+1:]
        #print("Before:",count)
        #print("A",A)
        #print("B",B)
        #print("C",C)
        quicksort_easy(A)
        quicksort_easy(C)
        #print("")
        #print("After:", count)
        #print("A",A)
        #print("B",B)
        #print("C",C)
        return A + [B] + C

#def quicksort_fast(X)



test = [4,7,1,23,57,0,-2]
quicksort_easy(test)
print(test)
