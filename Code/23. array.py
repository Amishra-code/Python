from array import *
vals=array('i',[5,9,8,4,2])

print(vals)

# i  ( signed int )
# I  ( unsigned int )

print(vals.buffer_info())                # provide address and size of array

print(vals.typecode)                     # i as in integer

vals.reverse()
print(vals)


vals.reverse()                           # again using the reverse function to make it original 
print(vals)

for i in range(5):
    print(vals[i])                       # i is index number here 

print()
for e in vals:
    print(e)

print()
for i in range(len(vals)):               # len(vals){is the length of array vals} = 5
    print(vals[i]) 


# creating new array from existing vals array
newArray=array(vals.typecode,(a for a in vals))

print()
for e in newArray:
    print(e)

newArray=array(vals.typecode,(a*a for a in vals))

print()
for e in newArray:
    print(e)

print()
i=0
while i<len(newArray):
    print(newArray[i])
    i+=1

# takin array values from the user
print() 
from array import *
arr=array('i',[])
n=int(input(" enter length : "))    

for i in range(n):
    x=int(input("enter the value : "))
    arr.append(x)
print(arr)    

val=int(input("enter the value for search : "))                 # searching of an element
k=0
for e in arr:
    if e==val:
        print(k)                                                # k is representing the index number
    k+=1    


# In python, array doesn't support multidimensional array. So, we will use numpy library.
print()
from numpy import *    
arr=array([1,2,3,4,5],int)                                        # int is optional to write 
print(arr)
print(arr.dtype)

print()
arr=array([1,2,3,4,5.0])                                          # here, the datatype will get changed to float
print(arr)
print(arr.dtype)  

arr=linspace(0,15,16)  
print(arr)                                           # stop in range is excluded but in linspace, it is included
# 0 : start
# 15 : stop
# 16 : step/ no. of parts

from numpy import arange
arr= arange(1,15,2)
print(arr)

arr=logspace(1,40,5)
print(arr)

# in linspace(), the difference between the two consecutive numbers is same but in logspace(),it is different

arr=logspace(1,40,5)
print('%.2f',arr[0])

from numpy import zeros
arr=zeros(5)
print(arr)

# adding two array elemets in an array

from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([6,1,9,3,2])

arr3=arr1+arr2
print(arr3)

from numpy import sin
print(sin(arr3))

arr3=arr3+5
print(arr3)

from numpy import sqrt
print(sqrt(arr3))

print(min(arr3))
print(max(arr3))

from numpy import unique
print(unique(arr3))

from numpy import concatenate
print(concatenate([arr1,arr2]))                 # concatenate() joins the two arrays into one array


# copying of an array

print()
print('normal copy')

arr1=array([2,6,8,1,3])
arr2=arr1

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


# 1. SHALLOW COPYING (uses view()) :
# it will copy the elements but then both the arrays are still dependent on one another  

print()
print('shallow copy')

arr1=array([2,6,8,1,3])
arr2=arr1.view()                               # view() helps to create the same element within an array at a different memory location 

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


# 2. DEEP COPYING ( uses copy()):
# copying of an array into one another in a way that they are not linked with each other in any way

print()
print('deep copy')

arr1=array([2,6,8,1,3])
arr2=arr1.copy()                               # view() helps to create the same element within an array at a different memory location 

arr1[1]=7

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))





