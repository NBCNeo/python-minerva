def merge_sortK(X,k):
    n = len(X)
    if n == 0 or n == 1:
        #conquer
        return X
    else:
        #divide
        size = int(n/k)
        r = n%k
        previous = 0
        larger = True
        container = []

        for j in range(k):
            if j >= r:
                larger = False
            container.append(merge_sortK(X[previous:previous+size+int(larger)],k)+[float('inf')])
            previous = previous+size+int(larger)

        #combine
        for i in range(n):
            firstelems = [sub[0] for sub in container]
            X[i] = min(firstelems)
            d = firstelems.index(X[i])
            container[d] = container[d][1:]

        return X

test = [23, 44, 52, 3, 5, 12, 45, 23, 46, 23, 56, 235, 6, 2346, 234, 56, 23456]
test2 = [23, 44, 52, 3, 5, 12, 45, 23, 46, 23, 56, 235, 6, 2346, 234, 56, 23456]
test2.sort()
print(merge_sortK(test,4) == test2)
