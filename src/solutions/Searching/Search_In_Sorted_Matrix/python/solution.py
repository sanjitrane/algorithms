# You're given a two-dimensional array (a matrix) of distinct integers and a
#   target integer. Each row in the matrix is sorted, and each column is also sorted; the
#   matrix doesn't necessarily have the same height and width.
#
#   Write a function that returns an array of the row and column indices of the
#   target integer if it's contained in the matrix, otherwise [-1, -1].
#
# Sample Input
#
# matrix = [
#   [1, 4, 7, 12, 15, 1000],
#   [2, 5, 19, 31, 32, 1001],
#   [3, 8, 24, 33, 35, 1002],
#   [40, 41, 42, 44, 45, 1003],
#   [99, 100, 103, 106, 128, 1004],
# ]
# target = 44
#
# Sample Output
# [3, 3]
#
# Time: O(n + m) | Space: O(1) - where n is the length of the matrix's rows and m is the length of the matrix's columns

def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]
