def max_heapify(A, i):
    n = len(A)
    l = 2*i+1
    r = l+1
    if l <= n-1:
        if A[l] > A[i]:
            largest = l
        else:
            largest = i
    else:
        largest = i
    if r <= n-1:
        if A[r] > A[largest]:
            largest = r
    if largest != i:
        x = A[i]
        A[i] = A[largest]
        A[largest] = x
        max_heapify(A, largest)

def build_max_heap(A):
    n = len(A)
    for i in range(int(n/2)-1,-1,-1):
        max_heapify(A, i)

Aexample = [39,85,85,16,49,7,49,92,76,15,21,30,29,31,28]

build_max_heap(Aexample)

print(Aexample)
