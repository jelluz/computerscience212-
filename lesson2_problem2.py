# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!






def longest_subpalindrome_slice(text):
    def length(a):
        return a[1]-a[0]

    def check_subpalindrome(text, i, j):
        if i >= 0 and j <= len(text):
            bla = "".join(reversed(text[i:j]))
            if text[i:j] == bla:
                longer =check_subpalindrome(text,i-1,j+1)
                if longer:
                    return longer
                else:
                    return (i,j)
        return False
    if text== "":
        return (0,0)
    if type(text) is not type("bla"):
        return (0,0)

    l = len(text)
    text = text.lower()
    longest = [0, -1, -1]
    longest = (0,0)
    dist=[2,3]
    for d in dist:
        for i in range(0, l - (d-1)):  # for each middel position-1
            j = i+d
            result = check_subpalindrome(text, i, j)
            if result and length(result) > length(longest):
                longest = result
    return longest


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print (test())




def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())
# test_check_subpalindrome()
