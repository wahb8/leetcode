

a = 123
a = [9] # --> 123 + 1 = 124 -> [1,2,4]

b = ""
print(len(a))


for i in range(len(a)):    
    b += str(a[i])
b = int(b)
b += 1

c = list(str(b)) # ['1','2','4'] list of 

def into(x, y):
    dod = 10 
    final = []
    for i in range(len(y)):
        final.append(x % dod)
        
        x = x // 10
    final = final [::-1]
    return final

print(into(b,c))

