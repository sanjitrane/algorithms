import unittest
from unittest import result
from solution import minRewards

TestResults = [
        {
          "Expected": 25
        },
        {
          "Expected": 1
        },
        {
          "Expected": 3
        },
        {
          "Expected": 3
        },
        {
          "Expected": 8
        },
        {
          "Expected": 9
        },
        {
          "Expected": 52
        },
        {
          "Expected": 15
        },
        {
          "Expected": 93
        }
      ] 
JSONTests = [
        {
          "scores": [
            8,
            4,
            2,
            1,
            3,
            6,
            7,
            9,
            5
          ]
        },
        {
          "scores": [
            1
          ]
        },
        {
          "scores": [
            5,
            10
          ]
        },
        {
          "scores": [
            10,
            5
          ]
        },
        {
          "scores": [
            4,
            2,
            1,
            3
          ]
        },
        {
          "scores": [
            0,
            4,
            2,
            1,
            3
          ]
        },
        {
          "scores": [
            2,
            20,
            13,
            12,
            11,
            8,
            4,
            3,
            1,
            5,
            6,
            7,
            9,
            0
          ]
        },
        {
          "scores": [
            2,
            1,
            4,
            3,
            6,
            5,
            8,
            7,
            10,
            9
          ]
        },
        {
          "scores": [
            800,
            400,
            20,
            10,
            30,
            61,
            70,
            90,
            17,
            21,
            22,
            13,
            12,
            11,
            8,
            4,
            2,
            1,
            3,
            6,
            7,
            9,
            0,
            68,
            55,
            67,
            57,
            60,
            51,
            661,
            50,
            65,
            53
          ]
        }
]

class MinRewardsTests(unittest.TestCase):
    def test_min_rewards(self):
        for i in range(0, len(JSONTests)):
            result = minRewards(JSONTests[i]['scores'])
            self.assertEqual(result, TestResults[i]['Expected'])