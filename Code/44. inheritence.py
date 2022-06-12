# 1. sinlge level inheritence
print()
class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B(A):

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")   

a1=A()
a1.feature1()
a2=A()
a2.feature2()

b3=B()
b3.feature3()
b4=B()
b4.feature4()
b2=B()
b2.feature2()
b1=B()
b1.feature1()



# 2. multi level inheritence
print()
class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B(A):

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working") 

class C(B):

    def feature5(self):
        print("Feature 5 working")

a1=A()
a1.feature1()
a2=A()
a2.feature2()

b3=B()
b3.feature3()
b4=B()
b4.feature4()
b2=B()
b2.feature2()
b1=B()
b1.feature1()

c5=C()
c5.feature5()


# 3. multiple inheritence
print()
class A:

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")    

class B:

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working") 

class C(A,B):

    def feature5(self):
        print("Feature 5 working")

a1=A()
a1.feature1()
a2=A()
a2.feature2()

b3=B()
b3.feature3()
b4=B()
b4.feature4()

c5=C()
c5.feature5()
c3=C()
c3.feature3()
c4=C()
c4.feature4()
c2=C()
c2.feature2()
c1=C()
c1.feature1()
