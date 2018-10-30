#heappush, heappop, and heapify

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

#heapq.heappush(heap, item)
#Push the value item onto the heap, maintaining the heap invariant.

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


#heapq.heappop(heap)
#Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

#heapq.heappushpop(heap, item)
#Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

Aexample = [39,85,85,16,49,7,49,92,76,15,21,30,29,31,28]

build_max_heap(Aexample)
print(Aexample)
heappush(Aexample,54)
print(Aexample)
print(heappop(Aexample))
print(Aexample)
