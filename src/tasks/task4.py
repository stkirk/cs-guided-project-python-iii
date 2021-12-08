# given an array of ints in ascending order and a target(int):
# find the indices of two integers that add up to the target
# return them in a list

def sumFinder(numbers, target):
    # create a dictionary to store {num:index} pairs
    num_dictionary = {}
    # loop through numbers
    for (i, num) in enumerate(numbers):
        # define what we're looking for, the index corresponding to complement
        complement = target - num
        # look up complement to see if it exists in dictionary
        if complement in num_dictionary:
            # if it exists in the dictionary return a list:
            # [num_dictionary[complement], i]
            return [num_dictionary[complement], i]
        # else add num to the dictionary
        else: 
            num_dictionary[num] = i
    # return error msg if no complements exist for a target
    return "No sums found"




print(sumFinder([3,8,12,16], 11)) # [0, 1]
print(sumFinder([3,4,5], 8)) # [0, 2]
print(sumFinder([0,1], 1)) # [0, 1]