# Write a function that takes in an array of at least three integers and,
# without sorting the input array, returns a sorted array of the three largest
# integers in the input array.
#
# The function should return duplicate integers if necessary; for example, it
# should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
# Sample Input
# array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# Sample Output
# [18, 141, 541]
#
# Time: O(n) | Space: O(1) - where n is the length of the input array

def threeLargestNumber(array):
    res = [None, None, None]

    for i in range(0, len(array)):
        if res[2] == None or res[2] < array[i]:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = array[i]
        elif res[1] == None or res[1] < array[i]:
            res[0] = res[1]
            res[1] = array[i]
        elif res[0] == None or res[0] < array[i]:
            res[0] = array[i]
    return res
