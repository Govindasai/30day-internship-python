set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Original sets:")
print(set1)
print(set2)
print("after removing using difference_update():")
set1.difference_update(set2)
print(set1)
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(set1-set2)
