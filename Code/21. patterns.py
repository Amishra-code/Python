
# # # # 
# # # #
# # # #
# # # #
for i in range (0,4):
    for j in range (0,4):
        print("#", end=" ")
    print()    
print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()        
print()

# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(1,6):
    for j in range(1,6-i):
        print(j,end=" ")
    print()    
print()    


# A
# A B
# A B C
# A B C D
for i in range(65,70):
    for j in range(65,i):
        a=chr(j)
        print(a,end=" ")
    print()
print() 


n=int(input("Enter number of rows to be printed: "))

x=n+64
print()


# A P Q R
# A B Q R
# A B C R
# A B C D
for i in range (65,x+1):

    for j in range (65,i+1):
        
        a=chr(j)
        print(a, end=" ")

    for k in range((j+15),  (x+15)):

        b=chr(k)
        print(b, end=" ")

    print()
