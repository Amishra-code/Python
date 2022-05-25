# swapping of two numbers

a=5
b=6
print("value of a before swapping = ",a)
print("value of b before swapping = ",b)

# method 1
a=a+b                     # 11/0b1011 (extra 1 bit is getting used)
b=a-b                     #  5/0b0101
a=a-b                     #  6/0b0110
print("value of a after swapping by method 1 = ",a)
print("value of b after swapping by method 1 = ",b)

# method 2
a=a^b
b=a^b
a=a^b
print("value of a after swapping by method 2 = ",a)
print("value of b after swapping by method 2 = ",b)

# method 3
a,b=b,a
# system will solve right side first (b,a). The values of 'b' and 'a' goes into a stack and then it reverse.
print("value of a after swapping by method 3 = ",a)
print("value of b after swapping by method 3 = ",b)