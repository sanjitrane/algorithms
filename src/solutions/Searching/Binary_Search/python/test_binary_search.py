import unittest
from solution import binarySearch

TestResults = [
    {
        "Expected": 3
    },
    {
        "Expected": 3
    },
    {
        "Expected": 1
    },
    {
        "Expected": -1
    },
    {
        "Expected": 0
    },
    {
        "Expected": 1
    },
    {
        "Expected": 2
    },
    {
        "Expected": 4
    },
    {
        "Expected": 6
    },
    {
        "Expected": 7
    },
    {
        "Expected": 8
    },
    {
        "Expected": 9
    },
    {
        "Expected": -1
    },
    {
        "Expected": 10
    },
    {
        "Expected": -1
    },
    {
        "Expected": -1
    },
    {
        "Expected": -1
    }
]
JSONTests = [
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 33
    },
    {
        "array": [
            1,
            5,
            23,
            111
        ],
        "target": 111
    },
    {
        "array": [
            1,
            5,
            23,
            111
        ],
        "target": 5
    },
    {
        "array": [
            1,
            5,
            23,
            111
        ],
        "target": 35
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 0
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 1
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 21
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 45
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 61
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 71
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 72
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 73
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73
        ],
        "target": 70
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73,
            355
        ],
        "target": 355
    },
    {
        "array": [
            0,
            1,
            21,
            33,
            45,
            45,
            61,
            71,
            72,
            73,
            355
        ],
        "target": 354
    },
    {
        "array": [
            1,
            5,
            23,
            111
        ],
        "target": 120
    },
    {
        "array": [
            5,
            23,
            111
        ],
        "target": 3
    }
]


class BinarySearchTest(unittest.TestCase):
    def test_binary_search(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            target = JSONTests[i]['target']
            result = binarySearch(array, target)
            self.assertEqual(result, TestResults[i]['Expected'])
