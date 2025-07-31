from collections import defaultdict

hash = defaultdict(int)

def contains(array):
    hashd = defaultdict(int)
    for i in array:
        hashd[i] += 1
    print(hashd)
    for i in array:
        if hashd[i] > 1:
            return False
        
    return True
array = [1,2,3,4,5,6,7,8,9]


print(contains(array))

def contains(array):
    x = set(list(array))
    if len(array) == len(x):
        return True
    else:
        return False
print(contains(array))
