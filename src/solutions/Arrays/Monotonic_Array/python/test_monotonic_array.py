import unittest
from unittest import result
from solution import monotonicArray, isMonotonic

TestResults = [
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
        "Expected": True
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
    },
    {
        "Expected": False
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
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    }
]
JSONTests = [
    {
        "array": [
            -1,
            -5,
            -10,
            -1100,
            -1100,
            -1101,
            -1102,
            -9001
        ]
    },
    {
        "array": []
    },
    {
        "array": [
            1
        ]
    },
    {
        "array": [
            1,
            2
        ]
    },
    {
        "array": [
            2,
            1
        ]
    },
    {
        "array": [
            1,
            5,
            10,
            1100,
            1101,
            1102,
            9001
        ]
    },
    {
        "array": [
            -1,
            -5,
            -10,
            -1100,
            -1101,
            -1102,
            -9001
        ]
    },
    {
        "array": [
            -1,
            -5,
            -10,
            -1100,
            -900,
            -1101,
            -1102,
            -9001
        ]
    },
    {
        "array": [
            1,
            2,
            0
        ]
    },
    {
        "array": [
            1,
            1,
            2,
            3,
            4,
            5,
            5,
            5,
            6,
            7,
            8,
            7,
            9,
            10,
            11
        ]
    },
    {
        "array": [
            1,
            1,
            2,
            3,
            4,
            5,
            5,
            5,
            6,
            7,
            8,
            8,
            9,
            10,
            11
        ]
    },
    {
        "array": [
            -1,
            -1,
            -2,
            -3,
            -4,
            -5,
            -5,
            -5,
            -6,
            -7,
            -8,
            -7,
            -9,
            -10,
            -11
        ]
    },
    {
        "array": [
            -1,
            -1,
            -2,
            -3,
            -4,
            -5,
            -5,
            -5,
            -6,
            -7,
            -8,
            -8,
            -9,
            -10,
            -11
        ]
    },
    {
        "array": [
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1,
            -1
        ]
    },
    {
        "array": [
            1,
            2,
            -1,
            -2,
            -5
        ]
    },
    {
        "array": [
            -1,
            -5,
            10
        ]
    },
    {
        "array": [
            2,
            2,
            2,
            1,
            4,
            5
        ]
    },
    {
        "array": [
            1,
            1,
            1,
            2,
            3,
            4,
            1
        ]
    },
    {
        "array": [
            1,
            2,
            3,
            3,
            2,
            1
        ]
    }
]


class MonotonicArrayTests(unittest.TestCase):
    def test_monotonic_array(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            result = monotonicArray(array)
            self.assertEqual(result, TestResults[i]['Expected'])

    def test_is_monotonic(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            result = isMonotonic(array)
            self.assertEqual(result, TestResults[i]['Expected'])
