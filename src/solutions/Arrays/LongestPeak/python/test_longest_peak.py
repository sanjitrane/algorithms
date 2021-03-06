import unittest
from unittest import result

from solution import longestPeak

TestResults = [
        {
          "Expected": 6
        },
        {
          "Expected": 0
        },
        {
          "Expected": 3
        },
        {
          "Expected": 6
        },
        {
          "Expected": 3
        },
        {
          "Expected": 5
        },
        {
          "Expected": 0
        },
        {
          "Expected": 0
        },
        {
          "Expected": 0
        },
        {
          "Expected": 4
        },
        {
          "Expected": 5
        },
        {
          "Expected": 9
        },
        {
          "Expected": 3
        }
      ]

JSONTests = [
        {
          "array": [
            1,
            2,
            3,
            3,
            4,
            0,
            10,
            6,
            5,
            -1,
            -3,
            2,
            3
          ]
        },
        {
          "array": [
            
          ]
        },
        {
          "array": [
            1,
            3,
            2
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5,
            1
          ]
        },
        {
          "array": [
            5,
            4,
            3,
            2,
            1,
            2,
            1
          ]
        },
        {
          "array": [
            5,
            4,
            3,
            2,
            1,
            2,
            10,
            12,
            -3,
            5,
            6,
            7,
            10
          ]
        },
        {
          "array": [
            5,
            4,
            3,
            2,
            1,
            2,
            10,
            12
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            10,
            100,
            1000
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
        },
        {
          "array": [
            1,
            1,
            3,
            2,
            1
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            2,
            1,
            1
          ]
        },
        {
          "array": [
            1,
            1,
            1,
            2,
            3,
            10,
            12,
            -3,
            -3,
            2,
            3,
            45,
            800,
            99,
            98,
            0,
            -1,
            -1,
            2,
            3,
            4,
            5,
            0,
            -1,
            -1
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            3,
            4,
            0,
            10
          ]
        }
      ]

class LongestPeakTests(unittest.TestCase):
    def test_longest_peak(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            result = longestPeak(array)
            self.assertEqual(result, TestResults[i]['Expected'] ) 