# Example 1: using the inner class
print()
class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    
    def show(self):
        print(self.name, self.rollno)


    class laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

s1=student('anjali',2) 
s2=student('anchal',1) 

s1.show()

s1.lap.brand
# OR
lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))



# Example 2: using method of the inner class  
print()
class student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand, self.cpu, self.ram)    

s1=student('anjali',2) 
s2=student('anchal',1) 

s1.show()

s1.lap.brand
# OR
lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))