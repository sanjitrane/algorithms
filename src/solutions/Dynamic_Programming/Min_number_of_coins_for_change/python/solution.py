# Given an array of positive integers representing coin denominations and a
#   single non-negative integer n representing a target amount of
#   money, write a function that returns the smallest number of coins needed to
#   make change for (to sum up to) that target amount using the given coin
#   denominations.
# 
#   Note that you have access to an unlimited amount of coins. In other words, if
#   the denominations are [1, 5, 10], you have access to an unlimited
#   amount of 1s, 5s, and 10s.
# 
#   If it's impossible to make change for the target amount, return
#   -1.
#  Sample Input
#  n = 7
#  denoms = [1, 5, 10]
# 
#  Sample Output
#  3 // 2x1 + 1x5
# 
# Time: O(nd) | Space: O(n) - where n is the target amount and d is the number of coin denominations

def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])
    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1