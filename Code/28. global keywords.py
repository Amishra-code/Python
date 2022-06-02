print()
print("1. preference will always be given to the local variable inside a function")
a=10
def something():
    a=15
    b=8
    print("in function a : ", a)

# print(b)                                          unresolved reference error

something()
print(" outside function a : ", a)


print()
print(2)
a=10
def something():

    global a                                        # hey python, my intention here is to update the global variable
    a=15
    print("in function a : ", a)

something()
print(" outside function a : ", a)


print()
print("3. if we want to use the concept of global and local in the same function, we will use a function globals(), and thereby we can access to all the gobal variables")
a=10
print(id(a))
def something():
    a=9

    x=globals()['a']   
    print(id(x))                                   
 
    print("in function a : ", a)

    globals()['a']=15                              # if we  change the value of x instead of a then a new variable x will get created and hence, global variable will not get updated

something()
print(" outside function a : ", a)

