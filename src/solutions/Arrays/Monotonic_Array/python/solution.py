
# Write a function that takes in an array of integers and returns a boolean
#   representing whether the array is monotonic.
#   An array is said to be monotonic if its elements, from left to right, are
#   entirely non-increasing or entirely non-decreasing.
#   Non-increasing elements aren't necessarily exclusively decreasing; they simply
#   don't increase. Similarly, non-decreasing elements aren't necessarily
#   exclusively increasing; they simply don't decrease.
# Note that empty arrays and arrays of one element are monotonic.
# Sample Input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Sample Output
# true
# Time: O(n) time | Space: O(1) - where n is the length of the array

def monotonicArray(array):
    if len(array) <= 2:
        return True
    dir = array[1] - array[0]
    for i in range(2, len(array)):
        if dir == 0:
            dir = array[i] - array[i-1]
            continue
        if breaksDir(dir, array[i-1], array[i]):
            return False
    return True


def breaksDir(dir, prevInt, currInt):
    diff = currInt - prevInt
    if dir > 0:
        return diff < 0
    else:
        return diff > 0


def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isIncreasing = False
        if array[i] > array[i - 1]:
            isDecreasing = False
    return isIncreasing or isDecreasing
