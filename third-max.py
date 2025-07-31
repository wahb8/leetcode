x = [3,6,4,6,3,98]

x = list(set(x))
x.sort()
x = x[::-1]
def find(arr):
        arr = list(set(arr))
        arr.sort()
        arr = arr[::-1]
        
        if (len(arr) >= 3):
            return arr[2]
        elif (len(arr) < 3):
            return arr[0]
        

print(find([3,2,1]))
