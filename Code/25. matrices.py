from array import *
from numpy import * 
from numpy import matrix

arr1=array([[1,2,3],
             [4,5,6]])

m = matrix(arr1)
print(m)

print()
m=matrix('1 2 3 6 ; 4 5 6 7')
print(m)

print()
m=matrix('1 2 3 ; 6 4 5 ; 7 8 9')
print(m)
print(diagonal(m))
print(m.max())

print()
m1=matrix('1 2 3 ; 6 4 5 ; 1 6 7')
m2=matrix('1 2 3 ; 6 8 5 ; 2 6 7')
m3=m1*m1
print(m3)
