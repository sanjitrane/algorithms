import unittest
from solution import numberOfWaysToMakeChange

TestResults = [
        {
          "Expected": 2
        },
        {
          "Expected": 1
        },
        {
          "Expected": 0
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
          "Expected": 13
        },
        {
          "Expected": 4
        },
        {
          "Expected": 3
        }
      ]
JSONTests = [
        {
          "denoms": [
            1,
            5
          ],
          "n": 6
        },
        {
          "denoms": [
            2,
            3,
            4,
            7
          ],
          "n": 0
        },
        {
          "denoms": [
            5
          ],
          "n": 9
        },
        {
          "denoms": [
            2,
            4
          ],
          "n": 7
        },
        {
          "denoms": [
            1,
            5,
            10,
            25
          ],
          "n": 4
        },
        {
          "denoms": [
            1,
            5,
            10,
            25
          ],
          "n": 5
        },
        {
          "denoms": [
            1,
            5,
            10,
            25
          ],
          "n": 10
        },
        {
          "denoms": [
            1,
            5,
            10,
            25
          ],
          "n": 25
        },
        {
          "denoms": [
            2,
            3,
            7
          ],
          "n": 12
        },
        {
          "denoms": [
            2,
            3,
            4,
            7
          ],
          "n": 7
        }
      ]

class MakeChangeTests(unittest.TestCase):
    def test_make_change(self):
        for i in range(0, len(JSONTests)):
            result = numberOfWaysToMakeChange(JSONTests[i]['n'], JSONTests[i]['denoms'])
            self.assertEqual(result, TestResults[i]['Expected'])