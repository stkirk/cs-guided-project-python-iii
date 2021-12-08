"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number_dumb(nums):
    for (i, num) in enumerate(nums):
        count = 1 #we've seen this number once, increment if it happens again
        # look through entire array and see if nums is duplicated
        for j in range(i + 1, len(nums)):
            if nums[j] == num:
                count += 1
        if count == 1:
                return num

def single_number_opt(nums):
    # use a dictionary to store how many times we've seen each number
    # the keys are the numbers (what we know)
    # the values are how many times we've seen that number (what we want to know)
    nums_dictionary = {num: 0 for num in nums} # dictionary comprehension
    for num in nums:
        # every time we see a number, increment it's value in the dictionary
        nums_dictionary[num] += 1
    # search the dictionary for key with value 1, this number only occurs once in nums
    for (key, val) in nums_dictionary.items():
        if val == 1:
            return key
    # Time complexity O(2n) == O(n)
    # Space complexity O(n)

def single_number_opt2(nums):
    # use an array to store values with no duplicates
    no_dupes = []
    for num in nums:
        if num in no_dupes:
            # remove if we find a duplicate
            no_dupes.remove(num)
        else:
            # otherwise we haven't seen this before so add it
            no_dupes.append(num)
    # wait until for loop is done to return
    return no_dupes.pop() #returns the last value of an array


# print(single_number_dumb([3,3,2]))
# print(single_number_dumb([5,2,3,2,3]))
# print(single_number_dumb([10]))

print(single_number_opt([3,3,2]))
print(single_number_opt([5,2,3,2,3]))
print(single_number_opt([10]))

print(single_number_opt2([3,3,2]))
print(single_number_opt2([5,2,3,2,3]))
print(single_number_opt2([10]))
