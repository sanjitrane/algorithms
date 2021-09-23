import unittest
from solution import longestRange

TestResults = [
        {
          "Expected": [
            0,
            7
          ]
        },
        {
          "Expected": [
            1,
            1
          ]
        },
        {
          "Expected": [
            1,
            2
          ]
        },
        {
          "Expected": [
            1,
            4
          ]
        },
        {
          "Expected": [
            1,
            4
          ]
        },
        {
          "Expected": [
            6,
            10
          ]
        },
        {
          "Expected": [
            10,
            19
          ]
        },
        {
          "Expected": [
            -1,
            19
          ]
        },
        {
          "Expected": [
            -7,
            7
          ]
        },
        {
          "Expected": [
            -8,
            19
          ]
        },
        {
          "Expected": [
            3,
            4
          ]
        },
        {
          "Expected": [
            -1,
            1
          ]
        },
        {
          "Expected": [
            0,
            1
          ]
        }
      ]
JSONTests = [
        {
          "array": [
            1,
            11,
            3,
            0,
            15,
            5,
            2,
            4,
            10,
            7,
            12,
            6
          ]
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
            4,
            2,
            1,
            3
          ]
        },
        {
          "array": [
            4,
            2,
            1,
            3,
            6
          ]
        },
        {
          "array": [
            8,
            4,
            2,
            10,
            3,
            6,
            7,
            9,
            1
          ]
        },
        {
          "array": [
            19,
            -1,
            18,
            17,
            2,
            10,
            3,
            12,
            5,
            16,
            4,
            11,
            8,
            7,
            6,
            15,
            12,
            12,
            2,
            1,
            6,
            13,
            14
          ]
        },
        {
          "array": [
            0,
            9,
            19,
            -1,
            18,
            17,
            2,
            10,
            3,
            12,
            5,
            16,
            4,
            11,
            8,
            7,
            6,
            15,
            12,
            12,
            2,
            1,
            6,
            13,
            14
          ]
        },
        {
          "array": [
            0,
            -5,
            9,
            19,
            -1,
            18,
            17,
            2,
            -4,
            -3,
            10,
            3,
            12,
            5,
            16,
            4,
            11,
            7,
            -6,
            -7,
            6,
            15,
            12,
            12,
            2,
            1,
            6,
            13,
            14,
            -2
          ]
        },
        {
          "array": [
            -7,
            -7,
            -7,
            -7,
            8,
            -8,
            0,
            9,
            19,
            -1,
            -3,
            18,
            17,
            2,
            10,
            3,
            12,
            5,
            16,
            4,
            11,
            -6,
            8,
            7,
            6,
            15,
            12,
            12,
            -5,
            2,
            1,
            6,
            13,
            14,
            -4,
            -2
          ]
        },
        {
          "array": [
            1,
            1,
            1,
            3,
            4
          ]
        },
        {
          "array": [
            -1,
            0,
            1
          ]
        },
        {
          "array": [
            10,
            0,
            1
          ]
        }
      ]

class LongestRangeTest(unittest.TestCase):
    def tests_longest_range(self):
        for i in range(0, len(JSONTests)):
            result = longestRange(JSONTests[i]['array'])
            self.assertEqual(result, TestResults[i]['Expected'])