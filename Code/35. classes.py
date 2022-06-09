# function in OOPs is called "methods"

# attributes ----> variables
# behaviour -----> methods (functions)


# Example 1
print()
class computer:

    def config(self):
        print("i5,16gb,1TB")

a=8
com1=computer()

print(type(a))                                          # <class 'int'>
print(type(com1))                                       # <class '__main__.computer'>


# NOTE : if we want to use a method, we need to mention the class name.
# Example 2
print()
class computer:

    def config(self):
        print("i5,16gb,1TB")
          
com1=computer()                                         # com1 : object

computer.config(com1)


# Example 3
print()
class computer:

    def config(self):
        print("i5,16gb,1TB")
          
com1=computer()  
com2=computer()                                     

computer.config(com1)
computer.config(com2)

com1.config()
com2.config()


# Example 4
print()
class computer:

    def __init__(self):
        print(" in init ")

    def config(self):
        print("i5,16gb,1TB")

com1=computer()  
com2=computer() 

com1.config()
com2.config()

# OUTPUT : 
#  in init
#  in init
# i5,16gb,1TB
# i5,16gb,1TB

# here we called two times the config function but we will get two times "in init" even thogh we didn't called the init function.
# This means "init" function will be automatically called for every object


# Example 5:
print()
class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is ", self.cpu, self.ram)

com1=computer('i5', 16)
com2=computer('Ryzen 3', 8)

com1.config()
com2.config()

# OUTPUT:
# Config is  i5 16
# Config is  Ryzen 3 8

# We are passing two values through the objects com1 and com2 to the class computer,
# but are accepting three parameters in the "_init_" method, 
# it is because "self" parameter acts as an acceptor for objects ( e.g. com1 OR com2) 






