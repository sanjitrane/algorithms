# Write a function that takes in an array of positive integers and returns the
# maximum sum of non-adjacent elements in the array.
# 
# If the input array is empty, the function should return 0.
# Sample Input
# array = [75, 105, 120, 75, 90, 135]
# 
# Sample Output
# 330 // 75 + 120 + 135
# 
# Time: O(n) time | O(1) space - where n is the length of the input array

def maxSubsetSumNoAdjacent(array):
    if len(array) == 0 :
        return 0
    elif len(array) == 1:
        return array[0]
    
    second = array[0]
    first = max(array[0], array[1])
    
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first
