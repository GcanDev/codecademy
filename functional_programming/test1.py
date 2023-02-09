nums = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)

# Checkpoint 1 code goes here.
greater_than_10_doubled=map(lambda x: x*2, filter(lambda x: x>10, nums))
print(tuple(greater_than_10_doubled))
# Translate this code into functional:
"""
lst = []
for i in nums:
  if i % 3 == 0:
    lst.append(i)
 
for i in range(len(lst)):
  lst[i] = lst[i] * 3
 
tuple(lst)
"""
# Checkpoint 2 code goes here.
functional_way=map(lambda x: x*3, filter(lambda x: x%3==0, nums))
print(tuple(functional_way))
