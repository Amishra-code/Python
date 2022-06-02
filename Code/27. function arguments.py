print()
print(1)
def update(x):
    x=8
    print("x",x)

a=10
update(a)
print("a",a)


print()
print(2)
def update(x):

    print(id(x))

    x=8
    print(id(x))
    print("x",x)

a=10
print(id(a))
update(a)
print("a",a)                     # address of a and x will diffr after the update in their values but x will not affect the value of x


print()
print(3)
def update(lst):
    print(id(lst))
    print(lst)

    lst[1]=25
    print(id(lst))
    print("x",lst)

lst=[10,20,30]
print(id(lst))
update(lst)
print("lst",lst)                # addresses of both the list will be same as the original gets affected by the argument of update function bcz list is mutable


print()
print('4. variable length')
def add(a,b):                   # a,b : formal arguments
    c=a+b
    print(c)

add(5,6)                        # 5,6 : actual parameters


print()
print(5)
def person(name,age):
    print(name)
    print(age)
person('anjali', 19)


print()
print('6. keyword')
def person(name,age):
    print(name)
    print(age)
person(name='anjali', age=19)


print()
print('7. default case')
def person(name,age=18):
    print(name)
    print(age)
person('anjali',19)


print()
print(8)
def sum(a, *b):                             # *b(single star) can accept multiple values
    print(a)
    print(b)

    c=a

    for i in b:
        c+=i
    print(c)

sum(5,6,34,78)


print()
print(9)
def sum(*b):                             
    
    print(b)

    c=0

    for i in b:
        c+=i
    print(c)

sum(5,6,34,78)


print()
print(10)
def person(name, *data):
    print(name)
    print(data)
person('anjali', 19, 'Meerut', 9876543210)


print()
print(10)
def person(name, **data):
    print(name)
    print(data)
person('anjali', age=19, city='Meerut', mob=9876543210)         # **data( double star): passing multiple values with the help of a keyword


print()
print(11)
def person(name, **data):
    print(name)

    for i,j in data.items():
         print(i,j)                                             # i : keyword , j : value pair

       
person('anjali', age=19, city='Meerut', mob=9876543210)












