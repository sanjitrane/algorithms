import unittest
from unittest import result
from solution import nonConstructibleChange

expectedOutput = [20, 6, 55, 3, 1, 1, 32, 19, 3, 1, 2, 87, 29]

JSONTests = [
    {
        "coins": [
            5,
            7,
            1,
            1,
            2,
            3,
            22
        ]
    },
    {
        "coins": [
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "coins": [
            1,
            5,
            1,
            1,
            1,
            10,
            15,
            20,
            100
        ]
    },
    {
        "coins": [
            6,
            4,
            5,
            1,
            1,
            8,
            9
        ]
    },
    {
        "coins": []
    },
    {
        "coins": [
            87
        ]
    },
    {
        "coins": [
            5,
            6,
            1,
            1,
            2,
            3,
            4,
            9
        ]
    },
    {
        "coins": [
            5,
            6,
            1,
            1,
            2,
            3,
            43
        ]
    },
    {
        "coins": [
            1,
            1
        ]
    },
    {
        "coins": [
            2
        ]
    },
    {
        "coins": [
            1
        ]
    },
    {
        "coins": [
            109,
            2000,
            8765,
            19,
            18,
            17,
            16,
            8,
            1,
            1,
            2,
            4
        ]
    },
    {
        "coins": [
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ]
    }
]


class NonConstructibleChangeTests(unittest.TestCase):
    def test_non_constructible_change(self):
        for i in range(0, len(JSONTests)):
            coins = JSONTests[i]['coins']
            result = nonConstructibleChange(coins)
            self.assertEqual(result, expectedOutput[i], 'Results')
