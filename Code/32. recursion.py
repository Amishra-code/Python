print()
def greet():                                    
    #print("hello")
    greet()                           # calling of a function itself, but the ouput will be limited to near about 1000, which will give an error in the end "maximum recursion depth exceeded"

greet()


# the way we can get the limit is by importing the 'sys' library
print()

import sys
#print(sys.getrecursionlimit())        # 996 nearest to 1000

def greet():                                    
    #print("hello")
    greet()

greet()


# increase the limit of recursion
print()

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())        # 1996 near to 2000

i=0
def greet():  

    global i
    i+=1                                  
    print("hello",i)
    greet()

greet()