# Write a function that takes in a non-empty string and that returns a boolean
# representing whether the string is a palindrome.
#
# A palindrome is defined as a string that's written the same forward and
# backward. Note that single-character strings are palindromes.
#
# Sample Input
# string = "abcdcba"
# Sample Output
# true // it's written the same forward and backward
# Time: O(n) | Space: O(1) - where n is the length of the input string

def isPalindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] != str[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
