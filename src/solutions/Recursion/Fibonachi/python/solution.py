# The Fibonacci sequence is defined as follows: the first number of the sequence
#   is 0, the second number is 1, and the nth number is the sum of the (n - 1)th
#   and (n - 2)th numbers. Write a function that takes in an integer
#   n and returns the nth Fibonacci number.
#
#   Important note: the Fibonacci sequence is often defined with its first two
#   numbers as F0 = 0 and F1 = 1. For the purpose of
#   this question, the first Fibonacci number is F0; therefore,
#   getNthFib(1) is equal to F0, getNthFib(2)
#   is equal to F1, etc..
# Sample Input #1
# n = 2
#
# Sample Output #1
# 1 // 0, 1
#
# Sample Input #2
# n = 6
#
# Sample Output #2
# 5 // 0, 1, 1, 2, 3, 5
#
# Time: O(n)  | Space: O(1) - where n is the input number

# Time: O(n) Space O(n)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 0
    if n == 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


# Time: O(n) Space O(1)


def fib1(n):
    lastTwo = [0, 1]
    counter = 3

    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
