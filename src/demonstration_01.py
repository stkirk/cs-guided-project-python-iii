"""
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # look through the array and for each number:
    # See if there is a complement for that number to add up to the target
    # num + complement == target
    for (i, num) in enumerate(nums): #-----------------> n
        complement = target - num #--------------------> 1
        # see if the complement exists in nums
        # use a starting point at nums[num] so we aren't being redundant
        # i.e. if no complement was found for nums[0] we can start our next iteration at nums[1] to the end the next time through.
        # ~ search from the rest of the list starting after i ~
        for complement_i in range(i + 1, len(nums)): #---> n
            if nums[complement_i] == complement: #-------> 1
                # return the indicies of num and the complement
                return [i, complement_i]

    return "No two sum solution"
    # Time complexity of this solution:
    # O(n + 1 * (n + 1)) == O(n^2 + n) --> BAD!!!
    # Space complexity: O(1)

# Optimize the solution for time complexity
def two_sum_opt(nums, target):
    # Plan: use a dictionary to remember what I've learned on my first loop through
    # The keys of the dictionary are numbers
    # The values of the dictionary are the numbers' corresponding indicies in nums
    # Can ask the dictionary "Where is a 5?", will return the index where 5 exists in nums
    nums_dictionary = {}
    for (i, num) in enumerate(nums):
        complement = target - num
        # look for complement within the dictionary
        if complement in nums_dictionary:
            # the first time a complement exists:
            return [nums_dictionary[complement], i]
        # once the search doesn't find a match, add the i to the dictionary for the next round
        # avoids matching with itself
        nums_dictionary[num] = i

    return "No two sum solution"
    # Time complexity of this solution:
    # O((n + 1) * (1)) == O(n) --> BETTER!!!
    # Space complexity: O(n)


print(two_sum([2,5,9,13], 7)) # [0, 1]
print(two_sum([4, 3, 5], 8)) # [1, 2]

print(two_sum_opt([2,5,9,13], 7)) # [0, 1]
print(two_sum_opt([4, 3, 5], 8)) # [1, 2]
