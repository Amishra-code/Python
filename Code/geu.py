#write a program that takes string as input and print words of having even length.

str=input("enter a string : ")
get=str.split()
for i in get:
    if(len(i)%2==0):
        print(i)