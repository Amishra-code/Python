# there r 2 types of variable:
# a)instance variable  b)class(static) variable

# Example 1:
print()
class car:
    def __init__(self):
        # mil and com are "instance variables"
        self.mil=10                 
        self.com="BMW"

c1=car()
c2=car()

print(c1.com, c1.mil)
print(c2.com, c2.mil)


# Example 2:
print()
class car:
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()

c1.mil=8

print(c1.com, c1.mil)
print(c2.com, c2.mil)


# Example 3:
print()
class car:
    # "wheels" are static variable
    wheels =4

    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()

c1.mil=8

print(c1.com, c1.mil,c1.wheels)
print(c2.com, c2.mil,c2.wheels)


# Example 4:
print()
class car:

    wheels =4

    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()

c1.mil=8

car.wheels=5

print(c1.com, c1.mil,c1.wheels)
print(c2.com, c2.mil,c2.wheels)


