# print(x(sqrt(25)))                   # error

import math
x=math.sqrt(25)
print(x)                               # no error

print(math.floor(2.9))                 # floor rounds off the number nearest to the digit before the decimal point
print(math.ceil(2.2))                  # ceil rounds off the number nearest to the next digit in decimal system

print(3**2)                            # pow(3,2) and output is in int
print(math.pow(3,2))                   #  output is in float

print(math.pi)
print(math.e)


# print(m.sqrt(25))                    # error
# CONCEPT OF ALLIES
import math as m
print(math.sqrt(25))
print(m.sqrt(25))                      # no error


# when we only want a certain function from the library
from math import sqrt,pow
print(pow(4,5))