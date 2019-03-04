import random



def random_biased(p):
    q = random.random()
    if q < p:
        return 1
    else:
        return 0


def random_unbiased():
    r = random.random()
    x1 = sum([random_biased(r) for t in range(100)])
    x2 = sum([random_biased(r) for s in range(100)])
    if x1 >= x2:
        return 1
    else:
        return 0

sums = []
for i in range(100):
    sums.append(sum([random_unbiased() for a in range(200)]))

print(sums)
