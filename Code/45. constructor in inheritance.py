# Example 1
print()
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B(A):

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")  

a1=B()   # prints "in A Init"                                                   



# Example 2
print()
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B(A):

    def __init__(self):
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")  

a1=B()   # prints "in B Init"                                                   



# Example 3
print()
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B(A):

    def __init__(self):
        super(). __init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")  

a1=B()   # prints "in A Init"
         # prints "in B Init"                                                  



# Example 4 : MRO ( Method Resolution Order), giving preference to left in multiple inheritence
print()
class A:

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B:

    def __init__(self):
        super(). __init__()
        print("in B Init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")  

class C(A,B):

    def __init__(self):
        super(). __init__()
        print("in C Init")

    def feature5(self):
        print("Feature 5 working")

a1=C()   # prints "in A Init"
         # prints "in C Init"      


