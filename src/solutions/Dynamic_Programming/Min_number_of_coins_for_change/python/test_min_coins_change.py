import unittest
from solution import minNumberOfCoinsForChange

TestResults = [
        {
          "Expected": 3
        },
        {
          "Expected": 3
        },
        {
          "Expected": 3
        },
        {
          "Expected": 0
        },
        {
          "Expected": 2
        },
        {
          "Expected": 4
        },
        {
          "Expected": 1
        },
        {
          "Expected": 2
        },
        {
          "Expected": 6
        },
        {
          "Expected": 3
        },
        {
          "Expected": -1
        },
        {
          "Expected": 1
        },
        {
          "Expected": 3
        },
        {
          "Expected": 2
        },
        {
          "Expected": 3
        },
        {
          "Expected": 2
        },
        {
          "Expected": 3
        }
      ]
JSONTests = [
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 7
        },
        {
          "denoms": [
            1,
            10,
            5
          ],
          "n": 7
        },
        {
          "denoms": [
            10,
            1,
            5
          ],
          "n": 7
        },
        {
          "denoms": [
            1,
            2,
            3
          ],
          "n": 0
        },
        {
          "denoms": [
            2,
            1
          ],
          "n": 3
        },
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 4
        },
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 10
        },
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 11
        },
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 24
        },
        {
          "denoms": [
            1,
            5,
            10
          ],
          "n": 25
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
            3,
            7
          ],
          "n": 7
        },
        {
          "denoms": [
            3,
            5
          ],
          "n": 9
        },
        {
          "denoms": [
            3,
            4,
            5
          ],
          "n": 9
        },
        {
          "denoms": [
            39,
            45,
            130,
            40,
            4,
            1
          ],
          "n": 135
        },
        {
          "denoms": [
            39,
            45,
            130,
            40,
            4,
            1,
            60,
            75
          ],
          "n": 135
        },
        {
          "denoms": [
            1,
            3,
            4
          ],
          "n": 10
        }
      ]

class MinCoinsChangeTests(unittest.TestCase):
    def test_min_coins_change(self):
        for i in range(0, len(JSONTests)):
            self.assertEqual((minNumberOfCoinsForChange(JSONTests[i]['n'], JSONTests[i]['denoms'])), TestResults[i]['Expected'])