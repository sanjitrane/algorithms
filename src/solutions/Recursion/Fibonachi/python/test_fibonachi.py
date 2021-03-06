import unittest
from unittest import result
from solution import fib, fib1


TestResults = [
    {
        "Expected": 5
    },
    {
        "Expected": 0
    },
    {
        "Expected": 1
    },
    {
        "Expected": 1
    },
    {
        "Expected": 2
    },
    {
        "Expected": 3
    },
    {
        "Expected": 8
    },
    {
        "Expected": 13
    },
    {
        "Expected": 21
    },
    {
        "Expected": 34
    },
    {
        "Expected": 55
    },
    {
        "Expected": 89
    },
    {
        "Expected": 144
    },
    {
        "Expected": 233
    },
    {
        "Expected": 377
    },
    {
        "Expected": 610
    },
    {
        "Expected": 987
    },
    {
        "Expected": 1597
    }
]
JSONTests = [
    {
        "n": 6
    },
    {
        "n": 1
    },
    {
        "n": 2
    },
    {
        "n": 3
    },
    {
        "n": 4
    },
    {
        "n": 5
    },
    {
        "n": 7
    },
    {
        "n": 8
    },
    {
        "n": 9
    },
    {
        "n": 10
    },
    {
        "n": 11
    },
    {
        "n": 12
    },
    {
        "n": 13
    },
    {
        "n": 14
    },
    {
        "n": 15
    },
    {
        "n": 16
    },
    {
        "n": 17
    },
    {
        "n": 18
    }
]


class FibonachiTest(unittest.TestCase):
    def test_fib(self):
        for i in range(0, len(JSONTests)):
            n = JSONTests[i]['n']
            result = fib(n)
            self.assertEqual(result, TestResults[i]['Expected'])

    def test_fib1(self):
        for i in range(0, len(JSONTests)):
            n = JSONTests[i]['n']
            result = fib1(n)
            self.assertEqual(result, TestResults[i]['Expected'])
