# we can pass function to other function, because in python, functions are objects
print()
f=lambda a:a*a
result=f(5)
print(result)

# these function are used with lamda
#filter()
#map()
#reduce()


print()
def is_even(n):
    return n%2==0

nums=[3,2,6,8,4,6,2,9]
evens=list(filter(is_even,nums))
print(evens)


# by using lambda
print()
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)


# using map
print()
def update(n):
    return n+2

nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)

print()
print("using map for update")
doubles=list(map(update,evens))
print(doubles)

print()
print("alternate way without using the user defined function and anonymus (lambda) ")
doubles=list(map(lambda n:n+2,evens))
print(doubles)



print()

from functools import reduce

def add(a,b):
    return a+b

nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)                                            # even = [2,6,8,4,6,2] 

doubles=list(map(lambda n:n*2,evens))
print(doubles)                                          # doubles = [4,12,16,8,12,4]

sum=reduce(add,doubles)
print(sum)

sum=reduce(lambda a,b : a+b,doubles)
print(sum)

# reduce function will add :
# 4+12=16
# 16+16=32
# 32+8=40
# 40+12=52
# 52+4=56 (final answer)

