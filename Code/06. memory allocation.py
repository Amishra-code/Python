num=5
print(id(num))

name='anjali'
print(id(name))

a=10
b=a
print(a)
print(b)

print(id(a))
print(id(b))
# same address of two variables containing same value hence python is more efficient
print(id(10))
# 'a' and 'b' are called "tags" as they are tagging same value 10

pi=3.14
print(pi)

pi=3.15
# we can change the value of a constant in python but we can show the intention to the other one not change it

print(type(pi))
