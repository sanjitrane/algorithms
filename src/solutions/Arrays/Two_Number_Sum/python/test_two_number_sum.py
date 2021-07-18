import unittest
from unittest import result

from solution import twoNumberSum, twoNumberSum2


jsonTests = [
    {
        "array": [
            3,
            5,
            -4,
            8,
            11,
            1,
            -1,
            6
        ],
        "targetSum": 10
    },
    {
        "array": [
            4,
            6
        ],
        "targetSum": 10
    },
    {
        "array": [
            4,
            6,
            1
        ],
        "targetSum": 5
    },
    {
        "array": [
            4,
            6,
            1,
            -3
        ],
        "targetSum": 3
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
        ],
        "targetSum": 17
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            15
        ],
        "targetSum": 18
    },
    {
        "array": [
            -7,
            -5,
            -3,
            -1,
            0,
            1,
            3,
            5,
            7
        ],
        "targetSum": -5
    },
    {
        "array": [
            -21,
            301,
            12,
            4,
            65,
            56,
            210,
            356,
            9,
            -47
        ],
        "targetSum": 163
    },
    {
        "array": [
            -21,
            301,
            12,
            4,
            65,
            56,
            210,
            356,
            9,
            -47
        ],
        "targetSum": 164
    },
    {
        "array": [
            3,
            5,
            -4,
            8,
            11,
            1,
            -1,
            6
        ],
        "targetSum": 15
    },
    {
        "array": [
            14
        ],
        "targetSum": 15
    },
    {
        "array": [
            15
        ],
        "targetSum": 15
    }
]

expectedOutput = [
    [11, -1],
    [4, 6],
    [4, 1],
    [6, -3],
    [8, 9],
    [3, 15],
    [-5, 0],
    [210, -47],
    [],
    [],
    [],
    []
]


class TwoNumberSumTests(unittest.TestCase):

    def test_TwoNumberSum(self):
        print(len(jsonTests))
        for item in range(0, len(jsonTests)):
            array = jsonTests[item]["array"]
            target = jsonTests[item]["targetSum"]
            result = twoNumberSum(array, target)
            testValue = set(result) == set(expectedOutput[item])
            self.assertTrue(testValue)

    def test_TwoNumberSum2(self):
        for item in range(0, len(jsonTests)):
            array = jsonTests[item]["array"]
            target = jsonTests[item]["targetSum"]
            result = twoNumberSum2(array, target)
            testValue = set(result) == set(expectedOutput[item])
            self.assertTrue(testValue)
