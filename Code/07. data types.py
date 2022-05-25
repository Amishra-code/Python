# none : variable which hasn't been assigned any value
# Numbers :
  # int
  # float
  # complex
  # bool

a=5.6
b=int(a)
print(type(b))
print(b)

k=6
c=complex(b,k)
print(c)
print(k<b)

bool=b<k
print(bool)
print(type(bool))

print(int(True))
print(int(False))

#list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list#

print(range(10))
print(list(range(10)))                    # 0-10 gets printed

print(list(range(2,10,3)))                # 10 doesn't gets printed also it's not fulfilling the condition
# 2 = start
# 10 = end
# 3 = difference

print(list(range(2,10,2)))                # 10 doesn't gets printed

#list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list*list#


d={'Anjali':'1+','Prerna':'Oppo','Arushi':'Realme'}
print(d.keys())
print(d.values())
print(d['Anjali'])



