import unittest
from unittest import result
from solution import isPalindrome

TestResults = [
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    }
]
JSONTests = [
    {
        "string": "abcdcba"
    },
    {
        "string": "a"
    },
    {
        "string": "ab"
    },
    {
        "string": "aba"
    },
    {
        "string": "abb"
    },
    {
        "string": "abba"
    },
    {
        "string": "abcdefghhgfedcba"
    },
    {
        "string": "abcdefghihgfedcba"
    },
    {
        "string": "abcdefghihgfeddcba"
    }
]


class PalindromeTest(unittest.TestCase):
    def test_isPalindrome(self):
        for i in range(0, len(JSONTests)):
            str = JSONTests[i]['string']
            result = isPalindrome(str)
            self.assertEqual(result, TestResults[i]['Expected'])
