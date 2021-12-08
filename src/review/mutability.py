# Mutability of lists

my_list1 = [1, 2, 3, 4]
# my_list2 points to the reference address of my_list1
# Shallow Copy - just copying the reference which causes unexpected mutations
my_list2 = my_list1

# verify both my_list1 & my_list2 have the same identity:
print("same identity? -->", my_list1 is my_list2)

# change my_list1 and you also change my_list1
my_list1.append(5)

print("still same identity? -->", my_list1 is my_list2)

"""
If we don't want to mutate other objects inadvertently like above, avoid using the equals assign. Must make a copy like using the spread operator in Javascript

Deep Copy - copy over the contents to a BRAND NEW OBJECT, without any lingering association to the original
"""
# copy of my_list1 using init dunder method from the list constructor
my_list3 = list(my_list1)
print("my_list1 and my_list3 same identity? -->", my_list1 is my_list3)
