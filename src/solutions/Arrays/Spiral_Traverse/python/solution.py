
# Write a function that takes in an n x m two-dimensional array (that can be
#   square-shaped when n == m) and returns a one-dimensional array of all the
#   array's elements in spiral order.
#   Spiral order starts at the top left corner of the two-dimensional array, goes
#   to the right, and proceeds in a spiral pattern all the way until every element
#   has been visited.
#   Sample Input
#   array = [
#   [1,   2,  3, 4],
#   [12, 13, 14, 5],
#   [11, 16, 15, 6],
#   [10,  9,  8, 7],
# ]
#
# Sample Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# Time: O(n) time | O(n) space - where n is the total number of elements in the array

def spiralTraverse(array):
    res = []
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1
    while startRow <= endRow and startCol <= endCol:
        #top - right
        for col in range(startCol, endCol + 1):
            res.append(array[startRow][col])
        # right - bottom
        for row in range(startRow+1, endRow + 1):
            res.append(array[row][endCol])
        #bottom-right - left
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            res.append(array[endRow][col])
        #bottom-left - top
        for row in reversed(range(startRow+1, endRow)):
            if startCol == endCol:
                break
            res.append(array[row][startCol])

        startCol += 1
        endCol -= 1
        startRow += 1
        endRow -= 1

    return res
