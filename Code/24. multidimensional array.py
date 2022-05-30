from array import *
from numpy import *

arr1 = array([[1,2,3],
             [4,5,6]])

print(arr1)

print(arr1.ndim)                                # finds no. of dimension
print(arr1.dtype)                               # data type
print(arr1.shape)                               # determines row and column
print(arr1.size)                                # gives size

print()
arr2=arr1.flatten()
print(arr2)

arr1=array([
               [1,2,3,6,2,9],
               [4,5,6,7,5,3]
            ])

print()
arr2=arr1.flatten()
print(arr2)

print()
arr3=arr1.reshape(3,4)                                # 3 rows and 4 columns 
print(arr3)

print()
arr3=arr2.reshape(2,2,3)                              # 2 multidimenional arrays each having 2 rows and 3 columns
