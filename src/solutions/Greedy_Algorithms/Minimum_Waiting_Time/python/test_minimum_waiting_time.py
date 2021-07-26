import unittest
from unittest import result
from solution import minimumWaitingTime

TestResults = [
    {
        "Expected": 17
    },
    {
        "Expected": 6
    },
    {
        "Expected": 23
    },
    {
        "Expected": 32
    },
    {
        "Expected": 10
    },
    {
        "Expected": 19
    },
    {
        "Expected": 45
    },
    {
        "Expected": 0
    },
    {
        "Expected": 0
    },
    {
        "Expected": 8
    },
    {
        "Expected": 1
    },
    {
        "Expected": 20
    },
    {
        "Expected": 20
    },
    {
        "Expected": 81
    },
    {
        "Expected": 10
    }
]
JSONTests = [
    {
        "queries": [
            3,
            2,
            1,
            2,
            6
        ]
    },
    {
        "queries": [
            2,
            1,
            1,
            1
        ]
    },
    {
        "queries": [
            1,
            2,
            4,
            5,
            2,
            1
        ]
    },
    {
        "queries": [
            25,
            30,
            2,
            1
        ]
    },
    {
        "queries": [
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "queries": [
            7,
            9,
            2,
            3
        ]
    },
    {
        "queries": [
            4,
            3,
            1,
            1,
            3,
            2,
            1,
            8
        ]
    },
    {
        "queries": [
            2
        ]
    },
    {
        "queries": [
            7
        ]
    },
    {
        "queries": [
            8,
            9
        ]
    },
    {
        "queries": [
            1,
            9
        ]
    },
    {
        "queries": [
            5,
            4,
            3,
            2,
            1
        ]
    },
    {
        "queries": [
            1,
            2,
            3,
            4,
            5
        ]
    },
    {
        "queries": [
            1,
            1,
            1,
            4,
            5,
            6,
            8,
            1,
            1,
            2,
            1
        ]
    },
    {
        "queries": [
            17,
            4,
            3
        ]
    }
]


class MinimumWaitingTimeTest(unittest.TestCase):
    def test_minimum_waiting_time(self):
        for i in range(0, len(JSONTests)):
            queries = JSONTests[i]['queries']
            result = minimumWaitingTime(queries)
            self.assertEqual(result, TestResults[i]['Expected'])
