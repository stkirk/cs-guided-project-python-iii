# Example 3

my_text1 = "Bloomtech"
my_text2 = my_text1

# same identity?
print("same identity?-->", my_text1 is my_text2)
print("same id?-->", "my_text1 id:", id(my_text1), "my_text2 id:", id(my_text2))

# change my_text1
my_text1 += "is awesome"
print("still same identity?-->", my_text1 is my_text2) #false
# strings are immutable, when we change my_text1 it points to a new reference, my_text2 still points to old reference
print("still same id?-->", "my_text1 id:", id(my_text1), "my_text2 id:", id(my_text2))

