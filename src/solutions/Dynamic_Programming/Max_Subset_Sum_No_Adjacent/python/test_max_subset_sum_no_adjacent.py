import unittest
from solution import maxSubsetSumNoAdjacent

TestResults =[
        {
          "Expected": 330
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
          "Expected": 15
        },
        {
          "Expected": 33
        },
        {
          "Expected": 207
        },
        {
          "Expected": 60
        },
        {
          "Expected": 90
        },
        {
          "Expected": 675
        },
        {
          "Expected": 180
        },
        {
          "Expected": 205
        },
        {
          "Expected": 72
        }
      ]
JSONTests =[
        {
          "array": [
            75,
            105,
            120,
            75,
            90,
            135
          ]
        },
        {
          "array": [
            
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
            1,
            2,
            3
          ]
        },
        {
          "array": [
            1,
            15,
            3
          ]
        },
        {
          "array": [
            7,
            10,
            12,
            7,
            9,
            14
          ]
        },
        {
          "array": [
            4,
            3,
            5,
            200,
            5,
            3
          ]
        },
        {
          "array": [
            10,
            5,
            20,
            25,
            15,
            5,
            5,
            15
          ]
        },
        {
          "array": [
            10,
            5,
            20,
            25,
            15,
            5,
            5,
            15,
            3,
            15,
            5,
            5,
            15
          ]
        },
        {
          "array": [
            125,
            210,
            250,
            120,
            150,
            300
          ]
        },
        {
          "array": [
            30,
            25,
            50,
            55,
            100
          ]
        },
        {
          "array": [
            30,
            25,
            50,
            55,
            100,
            120
          ]
        },
        {
          "array": [
            7,
            10,
            12,
            7,
            9,
            14,
            15,
            16,
            25,
            20,
            4
          ]
        }
      ]

class MaxSubsetSumNoAdjacentTests(unittest.TestCase):
    def test_max_subset_sum_no_adjacent(self):
        for i in range(0, len(JSONTests)):
            result = maxSubsetSumNoAdjacent(JSONTests[i]['array'])
            self.assertEqual(result, TestResults[i]['Expected'])