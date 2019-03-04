#Direct address tables
'''

Tup = ['steve','cake','icecream','mary','tom']
Tacross = ['peter','games', 'esther','randy','susan']

n_up = len(Tup)
n_across = len(Tacross)

Tguess = ['' for i in range(n_up+n_across)]

#we can insert a for or while loop here
ith_entry = int(input('what entry number do you want to set a guess for? '))
guess = input('what is your guess? ')
N[ith_entry] = guess

#clearing incorrect entries
for x in range(n_up+n_across):
    #up
    if x<n_up:
        if N[x] != Tup[x]:
            N[x] = ''
    #across
    else:
        if N[x] != Tacross[x-n_up]:
            N[x] = ''

'''

#Chained Hash-table

import random
import string


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


def empty_hash_table(N):
    return [[] for n in range(N)]


def add_to_hash_table(hash_table, item, hash_function):
    N = len(hash_table)
    if hash_function(item) >= 0 and hash_function(item) <= N:
        hash_table[hash_function(item)].append(item)
    
    return hash_table


def contains(hash_table, item, hash_function):
    N = len(hash_table)
    if hash_function(item) >= 0 and hash_function(item) <= N:
            return True if item in hash_table[hash_function(item)] else False
            
    else:
        print('hash function is not assigning a value within the range')


def remove(hash_table, item, hash_function):
    if not contains(hash_table, item, hash_function):
        raise ValueError()
    hash_table[hash_function(item)].remove(item)
    return hash_table


def hash_str1(string):
    ans = 0
    for chr in string:
        ans += ord(chr)
    return ans


def hash_str2(string):
    ans = 0
    for chr in string:
        ans = ans ^ ord(chr)
    return ans


def hash_str3(string):
    ans = 0
    for chr in string:
        ans = ans * 128 + ord(chr)
    return ans


def hash_str4(string):
    random.seed(ord(string[0]))
    return random.getrandbits(32)


Thash1 = [[] for x in range(5000)]
Thash2 = [[] for x in range(5000)]
Thash3 = [[] for x in range(5000)]
Thash4 = [[] for x in range(5000)]

all_words = [randomword(10) for i in range(100000)]

for word in all_words:
    add_to_hash_table(Thash1, word, hash_str1)
    add_to_hash_table(Thash2, word, hash_str2)
    add_to_hash_table(Thash3, word, hash_str3)
    add_to_hash_table(Thash4, word, hash_str4)

collisions1
for slot in Thash1:
    collisions+=len(slot)-1

collisions2
for slot in Thash2:
    collisions+=len(slot)-1

collisions3
for slot in Thash3:
    collisions+=len(slot)-1

collisions4
for slot in Thash4:
    collisions+=len(slot)-1

def elements_average(Thash,collisions):
    return (len(Thash)+collisions)/len(Thash)

#Answers
    
