def fact(n):
    fact=1

    for i in range(1,n+1):
        fact=fact*i

    return fact

x=5
result=fact(x)
print(result)