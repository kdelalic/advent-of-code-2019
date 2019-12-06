"""
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 136818-685979.
"""

import re

def isValid(number):
    num = str(number)

    # Check if digits are increasing
    prev = ""
    for i in num:
        if i < prev:
            return False
        prev = i
    
    # Check for adjacent digits
    matches = re.findall('00+|11+|22+|33+|44+|55+|66+|77+|88+|99+', num)

    # Check that there is atleast one pair of adjacent digits
    return matches and min(len(match) for match in matches) == 2

validNumbers = [num for num in range(136818, 685979) if isValid(num)]

print(len(validNumbers))
