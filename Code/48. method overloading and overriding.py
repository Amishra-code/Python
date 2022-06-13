# method overloading
print()
class student:

    def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a    
        return s


s1=student()

print(s1.sum(5,9,6))
print(s1.sum(5,9))
print(s1.sum(5))


# method overriding
# 1.
print()
class A:
    def show(self):
        print("in A show")

class B(A):
    pass

a1=B()
a1.show()     # prints "in A show"


# 2.
print()
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1=B()
a1.show()     # prints "in B show"