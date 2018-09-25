''' Insertion sort '''
import time
start_time = time.time()


def insertion_sort(l):
    steps = {'c1': 1, 'c2': 0, 'c3': 0, 'c4': 1, 'c5': 0, 'c6': 0, 'c7': 0}

    for j in range(1, len(l)):  # c1
        k = l[j]  # c2
        i = 0  # c3
        steps["c1"] += 1
        steps["c2"] += 1
        steps["c3"] += 1
        while k > l[i] and i < j:  # c4
            i += 1  # c5
            steps["c4"] += 1
            steps["c5"] += 1
        l.insert(i, k)  # c6
        l.pop(j+1)  # c7
        steps["c6"] += 1
        steps["c7"] += 1
    s = ''.join([str(steps[e])+e+' + ' for e in steps])[:-3]
    print(s)
    return (len(l), sum([steps[e] for e in steps]))


def bubbleSort(alist):
    steps = {'c1': 1, 'c2': 1, 'c3': 0, 'c4': 1, 'c5': 0, 'c6': 0}
    for passnum in range(len(alist)-1, 0, -1):  # c1
        steps["c1"] += 1
        for i in range(passnum):  # c2
            steps["c2"] += 1
            steps["c3"] += 1
            if alist[i] > alist[i+1]:  # c3
                temp = alist[i]  # c4
                alist[i] = alist[i+1]  # c5
                alist[i+1] = temp  # c6
                steps["c4"] += 1
                steps["c5"] += 1
                steps["c6"] += 1
    s = ''.join([str(steps[e])+e+' + ' for e in steps])[:-3]
    print(s)
    return (len(alist), sum([steps[e] for e in steps]))

def selectionSort(alist):
    steps = {'c1': 1, 'c2': 0, 'c3': 1, 'c4': 1, 'c5': 0, 'c6': 0, 'c7': 0, 'c8':0}
    for fillslot in range(len(alist)-1,0,-1):
        steps["c1"] += 1
        positionOfMax=0
        steps["c2"] += 1
        for location in range(1,fillslot+1):
            steps["c3"] += 1
            steps["c4"] += 1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
                steps["c5"] += 1

    temp = alist[fillslot]
    alist[fillslot] = alist[positionOfMax]
    alist[positionOfMax] = temp


print("--- %s seconds ---" % (time.time() - start_time))


def plotting(a):
    print(a)

# 40c1 + 39c2 + 39c3 + 429c4 + 428c5 + 39c6 + 39c7


lista1 = [23, 44, 52, 3, 5, 12, 45, 23, 46, 23, 56, 235, 6, 2346, 234, 56, 23456, 234, 623, 46,
          2346, 234, 6, 2346234, 62, 34, 61346, 234, 6, 2346, 346, 2, 354, 6, 2341, 346, 1, 346, 1, 34]
lista2 = [23, 44, 52, 3, 5, 12, 45, 23, 46, 23, 56, 235, 6, 2346, 234, 56, 23456, 234, 623, 46,
          2346, 234, 6, 2346234, 62, 34, 61346, 234, 6, 2346, 346, 2, 354, 6, 2341, 346, 1, 346, 1, 34]
# lista1.sort()
insertion_sort(lista2)
bubbleSort(lista2)

# print(lista1 == lista2)
