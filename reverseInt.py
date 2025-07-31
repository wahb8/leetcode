# 123 --> 321


x = 1534236469



def reverse(x):
    isNegative = False
          #1534236469 
    if x > 2147483647 or x < -2147483647:
        return 0
    
    if x >= 0:
        x = list(str(x))
    elif x < 0:
        x *= -1
        x = list(str(x))
        isNegative = True
    
        
    i = len(x) - 1
    a = ""
    
    while i >= 0:
        if x[i] != 0:
            a += x[i]
            i -= 1
        
    


    if isNegative == False:
        return int(a)
    else:
        return int(a) * -1


print(reverse(x))
