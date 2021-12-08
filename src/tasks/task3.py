# given two strings that only include lower case alpha chars:
# return a new string that contains any character that that appeared in str_1 or str_2
# characters may only appear in the new string once
# sort the new string alphabetically

# using join() + sorted()
# Sorting a string 
# res = ''.join(sorted(test_string))

def stringCondenser(str_1, str_2):
    # add strings together
    combined = str_1 + str_2
    print("combined-->", combined)
    # create solution string
    condensedStr = ""
    # loop through combined string
    for letter in combined:
        # print("letter-->", letter)
        # print("letter in condensed-->", letter in condensedStr)
        # conditional if letter in condensedStr string - continue
        if letter in condensedStr:
            continue
        # else add letter to combined string
        else:
            condensedStr += letter
    # sort and return
    print("sorted-->", ''.join(sorted(condensedStr)))
    return ''.join(sorted(condensedStr))

print(stringCondenser("aabbbcccdef", "xxyyzzz")) # 'abcdefxyz'
print(stringCondenser("xxyyzzz", "aabbbcccdef")) # 'abcdefxyz'
print(stringCondenser("abc", "abc")) # 'abc'
