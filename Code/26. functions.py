# Example 1
print()
def greet():                                    # def : definition 
    print("hello")
    print("good morning")

greet()                                         # function call


# Example 2
print()
def sum(x,y):
    c=x+y
    print(c)

sum(4,5)


# Example 3
print()
def sum(x,y):
    c=x+y
    return c
result=sum(4,5)
print(result)

# Example 4
print()
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)


