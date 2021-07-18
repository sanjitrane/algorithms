# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.
# Sample Input
# array = [1, 2, 3, 5, 6, 8, 9]
# Sample Output
# [1, 4, 9, 25, 36, 64, 81]
# Time: O(n) | Space: O(n) - where n is the length of the input
#

def sortedSquareArray(array):
    start = 0
    end = len(array) - 1
    res = [0] * len(array)
    while start <= end:
        pos = end - start
        val1 = array[start] * array[start]
        val2 = array[end] * array[end]
        if val1 > val2:
            res[pos] = val1
            start += 1
        else:
            res[pos] = val2
            end -= 1
    return res
