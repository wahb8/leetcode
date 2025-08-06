# we just wanna do x^n but x is a float

def pow(x,n):
    o = x ** n
    f = str(o)
    f = f"{o:.5f}"
    return float(f) 

print(pow(2.00000,10))

