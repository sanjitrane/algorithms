#
# Write a function that takes in a non-empty array of distinct integers and an
# integer representing a target sum. If any two numbers in the input array sum
# up to the target sum, the function should return them in an array, in any
# order. If no two numbers sum up to the target sum, the function should return
# an empty array.
# Note that the target sum has to be obtained by summing two different integers
# in the array; you can't add a single integer to itself in order to obtain the
# target sum.
# You can assume that there will be at most one pair of numbers summing up to
# the target sum.
#
# Sample Input = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10
#
# Sample Output
# [-1, 11] // the numbers could be in reverse order
# To Test: python test_two_number_sum.py
#

# Time: O(n) | Space: O(n)

def twoNumberSum(array, sum):
    nums = {}
    for num in array:
        potentialMatch = sum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# Time: O(nlog(n)) | Space: O(1)


def twoNumberSum2(array, sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        potentialMatch = array[left] + array[right]
        if potentialMatch == sum:
            return [array[left], array[right]]
        elif potentialMatch < sum:
            left += 1
        else:
            right -= 1
    return []
