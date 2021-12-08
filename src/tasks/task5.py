# given 2 strings, str_1 & str_2 where str_2 is a shuffled version of str_1 with one letter added at random:
# return the letter that was added to str_1 to get str_2

def addedLetterFinder(str_1, str_2):
    # create a list of letters from str_2
    str_2_list = list(str_2)
    # loop through str_1
    for letter in str_1:
        # if letter (in str_1) in str_2_list
        if letter in str_2_list:
            # remove the letter from str_2_list
            str_2_list.remove(letter)
    # return str_2_list only remaining index
    return str_2_list.pop()

print(addedLetterFinder("bcde", "bdcef")) #--> 'f'
print(addedLetterFinder("", "z")) #--> 'z'
print(addedLetterFinder("b", "bb")) #--> 'b'
print(addedLetterFinder("bf", "bfb")) #--> 'b'