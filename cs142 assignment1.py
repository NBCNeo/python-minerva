import threading

def state_00(s):
    tname = threading.currentThread().getName()
    print('\t',tname, 'enters state 2 with s=',s)
    if len(s) == 0:
        tname = threading.currentThread().getName()
        print('******',tname, 'reached accept state 000 ***')
        return True
    else:
        if s[0] in 'afg':
            state_00(s[1:])
        if s[0]=='e':
            state_01(s[1:])

def state_11(s):
    tname = threading.currentThread().getName()
    print('\t',tname, 'enters state 2 with s=',s)
    if len(s) > 0:
        if s[0] in 'bch':
            state_11(s[1:])
        if s[0]=='d':
            state_10(s[1:])

def state_10(s):
    tname = threading.currentThread().getName()
    print('\t',tname, 'enters state 2 with s=',s)
    if len(s) == 0:
        tname = threading.currentThread().getName()
        print('******',tname, 'reached accept state 000 ***')
        return True
    else:
        if s[0] in 'afg':
            state_00(s[1:])
        if s[0]=='e':
            state_01(s[1:])

def state_01(s):
    tname = threading.currentThread().getName()
    print('\t',tname, 'enters state 2 with s=',s)
    if len(s) > 0:
        if s[0] in 'bch':
            state_11(s[1:])
        if s[0]=='d':
            state_10(s[1:])


def N1(s):
    n=len(s)
    threads=[]
    print('N1 computes input string',s)
    print('\t N1 spliting computation with input :',s,'in two branches')
    t1 = threading.Thread(target=state_00, args=[s])
    threads.append(t1.name)
    t1.start()

    t2 = threading.Thread(target=state_10, args=[s])
    threads.append(t2.name)
    t2.start()

s = 'a'
print(N1(s))
print('HERE',threading.active_count())
