"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 136818-685979.
"""

import math, re

def hasAdjacentDigits(number):
    num = str(number)
    matches = re.findall('00+|11+|22+|33+|44+|55+|66+|77+|88+|99+', num)

    return bool(matches)

def hasIncreasingDigits(number):
    num = str(number)
    prev = ""
    for i in num:
        if i < prev:
            return False
        prev = i

    return True

adjacentDigits = [num for num in range(136818, 685979) if hasAdjacentDigits(num)]

increasingDigits = [num for num in adjacentDigits if hasIncreasingDigits(num)]

print(len(increasingDigits))