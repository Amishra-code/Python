i=1                     # initialization
while i<=5:             # condition
    print("Anjali")
    i=i+1               # increament / decreament



# NESTED (while)
# Example 2(a) :
i=1
j=1
while i<=5:
    print("Telusko", end=" ")
    while j<=4:
        print("Rocks", end=" ")
        j=j+1
    i=i+1
# end is used so that the new output doesn't jumps on the new line but stays on the same line

# Example 2(b)
print()                # for new line
i=1
while i<=5:
    print("Telusko", end=" ")
    j = 1
    while j<=4:
        print("Rocks", end=" ")
        j=j+1
    i=i+1
    print()