# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# . means matching any charcter
# * means matches zero or more of the proceeding charcters

# s = 'aa', p = 'a' --> false
# s = 'aa', p = 'a*' --> true (becuase a* means like (a until you find a match)
# s = 'asdasdas', p = '.*' --> true 

# run for the length of s?

def star(txt):
    pass

def regex(s, p):
    if s == p:
        return True
    
    memo = {}

    if "*" in p:
        index = p.find("*")
        char = p[index - 1]
        
        string = char * len(s)
        
        print(string)
        return (s in string)
        

print(regex("aaaaaaaaaaaaaaaaaaaa","a*"))

