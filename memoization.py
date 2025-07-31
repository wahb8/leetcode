



memo = {}

def fib(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n

    else:
        memo[n] = fib(n-2) + fib(n-1)

    print(memo)
    return memo[n]


print(fib(5))
