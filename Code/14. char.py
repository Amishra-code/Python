ch = input("enter a character : ")
print(ch)                          # can take more than 1 chararcter and will also provide the same output

ch = input("enter a character : ")
print(ch[0])                       # can take more than 1 character as input but will print only 1 character

ch = input('enter a character : ')[0]
print(ch)                          # will take only 1 character as input so will print only 1 character


# to evaluate ( 2 + 6 - 1 ) type of statement
result = eval(input("enter an expression : "))
print(result)                      # output : 7