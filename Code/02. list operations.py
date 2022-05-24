#list : mutable (values can get changed unlike arrays in c)

names=['anjali','mishra']
print(names)

nums=[25,12,36,95,14]
print(nums)

mil=[nums,names]
print(mil)

#inbuilt functions for list

nums.append(45)             # append:adds any element at the end of the list
print(nums)

nums.remove(14)             # 14: an element of the list
print(nums)

nums.pop(1)                 # 1: index number
print(nums)

del nums[2:]                
print(nums)

# nums.extend(29,12,14,36)  #error
# print(nums)
# this is differently used without a dot(.)

nums.extend([29,12,14,36])  # remember to use [] bracket for extend case
print(nums)

print(min(nums))            # smallest element of the list

print(max(nums))            # largest element of the list

print(sum(nums))            # sum of all the elements in the list

# print(nums.sort)          # error

nums.sort()                 # by default sorts in asccending order
print(nums)
