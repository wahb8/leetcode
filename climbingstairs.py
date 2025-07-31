


def climbing(n):

    if n <= 2:
        return n
    
    a, b = 1, 2

    for i in range(3,n+1):
        a, b = b, a + b # 2, 3
                        # 3, 5
                        
        print(11)
    return b


def climbing(n, memo={}):
    if n in memo:
        return memo[n] 
    
    if n <= 2:
        memo[n] = n
    else:
        memo[n] = (climbing(n-1) + climbing (n-2)) 
    return memo[n]

def climbing1(n):
    if n <= 2:
        return n
    return (climbing1(n-1) + climbing1(n-2))


#print(climbing(353))
print(climbing1(353))
