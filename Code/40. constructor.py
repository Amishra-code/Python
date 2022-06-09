# Example 1:
print() 
class Computer:
    pass

c1=Computer()                    # Computer is a "constructor"                      
print(id(c1))                    # 2617355788192

c2=Computer()
print(id(c2))                    # 2617355788144


# Example 2:
print()
class Computer:
    def __init__(self):
        self.name='anjali'
        self.age=18
    

c1=Computer()                                   
c2=Computer()                   

print(c1.name)
print(c2.name)


# Example 3:
print()
class Computer:
    def __init__(self):
        self.name='anjali'
        self.age=18
    
    def update(self):             # we aren't passing any parameter in [c1.update()], so self will start pointing towars c1
        self.age=19               # self is the current instance

c1=Computer()                       
c2=Computer() 

c1.name='Deeksha'
c1.age=27

c1.update()

print(c1.name)
print(c1.age)

print(c2.name)
print(c2.age)


# Example 4:
print()
class Computer:
    def __init__(self):
        self.name='anjali'
        self.age=18
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else: 
            return False    

c1=Computer()                       
c2=Computer() 

if c1==c2:                                       # "They are different" because these are the two different objects which acts as pointers
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)


# Example 4:
print()
class Computer:
    def __init__(self):
        self.name='anjali'
        self.age=18
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else: 
            return False    

c1=Computer()                       
c2=Computer() 

if c1.compare(c2):                                 # They are same
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)


# Example 5:
print()
class Computer:
    def __init__(self):
        self.name='anjali'
        self.age=18
    
    def compare(self,other):                      # compare (who is calling,whom to compare)
        if self.age == other.age:
            return True
        else: 
            return False    

c1=Computer()
c1.age=19                       
c2=Computer() 

if c1.compare(c2):                                # They are different
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)








