import heapq

def add_to_median_heap(minh, maxh, elem):
    heapq.heappush(minh,elem)
    heappush(maxh,elem)

def median(minh,maxh):
    pass

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

def heappush(heap, item):
    heap.append(item)
    i = len(heap)-1
    while i > 0 and heap[i//2-(1-i%2)] < heap[i]:
        placeholder = heap[i]
        heap[i] = heap[i//2-(1-i%2)]
        heap[i//2-(1-i%2)] = placeholder
        i = i//2-(1-i%2)

def heappop(heap):
    max = heap[0]
    heap[0] = -float('inf')
    max_heapify(heap,0)
    heap.pop(len(heap)-1)
    return max

def heappushpop(heap, item):
    max = max(heap[0], item)
    heap[0]=item
    max_heapify(heap,0)
    return max

Aexample1 = [3,8,5,16,19,7,9,2,15,21,25,31,8]
Aexample2 = Aexample1[:]

build_max_heap(Aexample1)
heapq.heapify(Aexample2)

#print(Aexample1)
#print(Aexample2)
