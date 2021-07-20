
# Write a function that takes in two non-empty arrays of integers, finds the
#   pair of numbers (one from each array) whose absolute difference is closest to
#   zero, and returns an array containing these two numbers, with the number from
#   the first array in the first position.
#   Note that the absolute difference of two integers is the distance between
#   them on the real number line. For example, the absolute difference of -5 and 5
#   is 10, and the absolute difference of -5 and -4 is 1.
#   You can assume that there will only be one pair of numbers with the smallest
#   difference.
# Sample Input
#
# arrayOne = [-1, 5, 10, 20, 28, 3]
# arrayTwo = [26, 134, 135, 15, 17]
# Sample Output
# [28, 26]
# Time O(nlog(n) + mlog(m)) | Space O(1) - where n is the length of the first input array and m is the length of the second input array

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0
    currentSum = float("inf")
    smallest = float("inf")
    pairs = []
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        fNum = arrayOne[p1]
        sNum = arrayTwo[p2]
        if fNum > sNum:
            currentSum = fNum - sNum
            p2 += 1
        elif sNum > fNum:
            currentSum = sNum - fNum
            p1 += 1
        else:
            return [fNum, sNum]
        if smallest > currentSum:
            smallest = currentSum
            pairs = [fNum, sNum]
    return pairs
