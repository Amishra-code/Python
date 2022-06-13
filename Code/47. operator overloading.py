# 1.
print()
a=5
b=6
print(a+b) #11 ( by default this add operator calls __add__() method)             
print(int.__add__(a,b)) #11


# 2.
print()
a='5'
b='6'
print(a+b) #56 ( by default this add operator calls __str__() method)             
print(str.__add__(a,b)) #56


# 3.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

s1=student(58,59)
s2=student(60,65)

# s3 = s1 + s2  ( unsupported operand )


# 4.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2) 
        return s3 

s1=student(58,59)
s2=student(60,65)

s3=s1+s2
print(s3.m1)


# 4.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __gt__(self,other):
        r1=self.m1+other.m1
        r2=self.m2+other.m2

        if r1>r2:
            return True
        else:
            return False    

s1=student(58,59)
s2=student(60,65)

if s1>s2:
    print("s1 wins") 
else:
    print("s2 wins") 


# 5.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2     

s1=student(58,59)
s2=student(60,65)

print(s1.__str__())     # <__main__.student object at 0x000002AF980F4FD0> : <module name.class name's object at address>


# 6.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2     
    
    def __str__(self):
        return self.m1   # will  print (58,59) which is a tupple
        
s1=student(58,59)
s2=student(60,65)

print(s1.__str__())


# 7.
print()
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2     
    
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)    # will print in the correct format : 58 59
        
s1=student(58,59)
s2=student(60,65)

print(s1)
