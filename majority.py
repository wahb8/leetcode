'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''


array = [3,2,3]
size = 3

def majority(array):
    n = len(array)
    m = n/2
    highest = 0
    hashm = {}

    for i in array:
        hashm[i] = 0

    for i in array:
        hashm[i] += 1

    for i in hashm:
        if hashm[i] > m:
            highest = i
            return highest
    
    
print(majority(array))

