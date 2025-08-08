







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
        print(i)
        if i in s:
            arr[i] = f'{i}s'
        elif i in h:
            arr[i] = f'{i}h' 

    return arr

print(makeList([1,2,5],[3]))

