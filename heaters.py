# LEETCODE PROBLEM HEATERS (MEDIUM)

# The problem we are trying to solve is the problem of finding the minimum radius a heaters can have so all the houses are heated
# We will get two inputs
# s = [1,2,3,4]
# which is the locations of all the houses we have

# h = [1,4]
# which is the locations of all the heaters we have

# we want to find the minimum radius a heater can have so all the houses are heated
# with the inputs we have, the minimum r would be 1
# since heater on location 1 can heat house 1 and 2
# and heater 4 can heat houses on location 4 and 3

def makeList(s, h):
    s.sort()
    h.sort()


    arr = []
    
    maxR = 0

    if (s[-1] > h[-1]):
        maxR = s[-1]
    else:
        maxR = h[-1]
    
    arr = [0] * (maxR + 1) 

    for i in range(maxR + 1):
        if i in h:
            arr[i] = f'{i}h'
        elif i in s:
            arr[i] = f'{i}s'


    return arr

print(makeList([1,2,5],[3]))
print(makeList([1,2,5],[2]))

def addTrees(tree1,tree2):

