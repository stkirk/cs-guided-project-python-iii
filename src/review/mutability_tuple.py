# Initialize a produce list(mutable):
produce = ["Apple", "Banana", "Carrot"]

# Initialize a tuple(immutable) and include a reference to the produce list:
store = ("Bill's Grocery", produce)
print("store id:", id(store))

# add to produce list:
produce.append("Dragonfruit")
print("store id:", id(store)) # tuple retains the same reference id
# The produce list is mutable, it can be changed and still point to the same reference. Thus the tuple store[1] is still pointing to the same reference for produce even though produce's value changed and the tuple isn't mutated
