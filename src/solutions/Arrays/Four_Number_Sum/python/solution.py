 # Write a function that takes in a non-empty array of distinct integers and an
 #   integer representing a target sum. The function should find all quadruplets in
 #   the array that sum up to the target sum and return a two-dimensional array of
 #   all these quadruplets in no particular order.
 #   If no four numbers sum up to the target sum, the function should return an
 #   empty array.
 #  Sample Input
 #  array = [7, 6, 4, -1, 1, 2]
 #  targetSum = 16
 #
 #  Sample Output
 # [[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
 #
 # Time: Average: O(n^2) | O(n^2) - where n is the length of the input array
 # Worst: O(n^3) time | O(n^2) space - where n is the length of the input array

def fourNumberSum(array, targetSum):
    allPairs = {}
    quads = []
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            diff = targetSum - currentSum
            if diff in allPairs:
                for pair in allPairs[diff]:
                    quads.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[k] + array[i]
            if currentSum not in allPairs:
                allPairs[currentSum] = [[array[k], array[i]]]
            else:
                allPairs[currentSum].append([array[k],array[i]])
    return quads