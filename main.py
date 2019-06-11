import random
def gen(a = 1):
    b = []
    for i in range(a):
        b.append(random.randint(-100, 100))
    return tuple(b)

def vstav(a):
    a = list(a)
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j] = a[j] + a[j-1]
                    a[j-1] = a[j] - a[j-1]
                    a[j] = a[j] - a[j-1]
    return a

def buble(a):
    a = list(a)
    q = False
    while not(q):
        q = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i] = a[i] + a[i+1]
                a[i+1] = a[i] - a[i+1]
                a[i] = a[i] - a[i+1]
                q = False
    return(a)

list1 = gen(10)

print(list1)
print(vstav(list1))
print(buble(list1))
print(sorted(list1))

def mda(q):
    a = []
    b = []
    for i in q:
        if i >=0:
            a.append(i)
        else:
            b.append(i)
    return a, b

print(mda(gen(10)))
