# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.
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
    
    if p == ".*":
        return True


    if "*" in p:
        index = p.find("*")
        char = p[index - 1]
        
        string = char * len(s)
        
        return (s in string)

    
    if len(p) != len(s):
        print("a")
        return False

    if "." in p and p != ".*":
        allc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
        index = p.find(".")
        
        if s[index] in allc:
            return True
    
    if p == ".*":
        return True












def regex(s, p):
        
    def dot()
        allc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
        index = p.find(".")
        
        if s[index] in allc:
            return True
    














        


print(regex("ab",".*"))

