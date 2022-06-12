# types of methods are :
# 1. instance methods 
#    a) accessor methods - fetch the value
#    b) mutator methods - modify the value
# 2. class methods
# 3. static methods 


# Example 1 (instance methods)
print()
class student:

    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

s1=student(34,67,32)
s2=student(89,32,23)

print(s1.avg())
print(s2.avg())


# Example 2 (instance methods - accessor, mutator)
print()
class student:

    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):                             # getters get the value : fetch the value
        return self.m1

    def set_m1(self,value):                       # setters set the value : change the value
        self.m1=value
    
s1=student(34,67,32)
s2=student(89,32,23)


# Example 3 (class methods)
print()
class student:

    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):                             
        return self.m1

    def set_m1(self,value):                       
        self.m1=value 

    @classmethod
    def info(cls):
        return cls.school       

s1=student(34,67,32)
s2=student(89,32,23)

print(student.info())


# Example 4 (static methods)
print()
class student:

    school='telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):                             
        return self.m1

    def set_m1(self,value):                       
        self.m1=value 

    @staticmethod
    def info():
        print("This is student class")       

s1=student(34,67,32)
s2=student(89,332,23)
student.info()
