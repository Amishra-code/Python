def fib(n):

    a=0
    b=1
    
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(5)


# if we want only the 1 term, we will get two terms, to get the correct output, follow the code given below
print()
def fib(n):

    a=0
    b=1
    
    if n==1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(1)


