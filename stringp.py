# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
from collections import defaultdict
s = "ada"
t = "aad"

def stri(s,y):
    s = list(s)
    y = list(y)


    hash1 = defaultdict(int)
    hash2 = defaultdict(int)
    
    for i in s:
        hash1[i] += 1

    for i in y:
        hash2[i] += 1
    
    return (hash1 == hash2)

print(stri(s,t))
        
