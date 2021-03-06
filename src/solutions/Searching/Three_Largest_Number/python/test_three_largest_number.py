import unittest
from unittest import result
from solution import threeLargestNumber

TestResults = [
    {
        "Expected": [
            18,
            141,
            541
        ]
    },
    {
        "Expected": [
            7,
            8,
            55
        ]
    },
    {
        "Expected": [
            11,
            43,
            55
        ]
    },
    {
        "Expected": [
            11,
            43,
            55
        ]
    },
    {
        "Expected": [
            11,
            43,
            55
        ]
    },
    {
        "Expected": [
            7,
            7,
            7
        ]
    },
    {
        "Expected": [
            7,
            7,
            8
        ]
    },
    {
        "Expected": [
            -2,
            -1,
            7
        ]
    }
]
JSONTests = [
    {
        "array": [
            141,
            1,
            17,
            -7,
            -17,
            -27,
            18,
            541,
            8,
            7,
            7
        ]
    },
    {
        "array": [
            55,
            7,
            8
        ]
    },
    {
        "array": [
            55,
            43,
            11,
            3,
            -3,
            10
        ]
    },
    {
        "array": [
            7,
            8,
            3,
            11,
            43,
            55
        ]
    },
    {
        "array": [
            55,
            7,
            8,
            3,
            43,
            11
        ]
    },
    {
        "array": [
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7,
            7
        ]
    },
    {
        "array": [
            7,
            7,
            7,
            7,
            7,
            7,
            8,
            7,
            7,
            7,
            7
        ]
    },
    {
        "array": [
            -1,
            -2,
            -3,
            -7,
            -17,
            -27,
            -18,
            -541,
            -8,
            -7,
            7
        ]
    }
]


class ThreeLargestNumbersTest(unittest.TestCase):
    def test_three_largest_numbers(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            result = threeLargestNumber(array)
            self.assertEqual(result, TestResults[i]['Expected'])
