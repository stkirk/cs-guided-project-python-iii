# given a string:
# return the index of the first occurence of a unique character 
# if there isn't a unique character return -1

# nums_dictionary = {num: 0 for num in nums}

def uniqueCharFinder(input_str):
    # create a dictionary where the key is a letter and the value is initialized at 0
    str_dictionary = {letter: 0 for letter in input_str}
    # loop through input_str again
    for letter in input_str:
        # for each letter increment the dictionary[letter] by 1
        str_dictionary[letter] += 1
    # print("dictionary-->", str_dictionary)
    # loop through again, enumerate
    for (i, letter) in enumerate(input_str):
    # return the first index where the corresponding value in the dictionary == 1 (first unique letter)
        if str_dictionary[letter] == 1:
            return i
    return -1

print(uniqueCharFinder("lambdaschool")) #--> 2
print(uniqueCharFinder("ilovelambdaschool")) #--> 0
print(uniqueCharFinder("vvv")) #--> -1