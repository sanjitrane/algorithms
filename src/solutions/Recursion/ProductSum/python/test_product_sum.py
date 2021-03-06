import unittest
from solution import productSum

TestResults = [
        {
          "Expected": 12
        },
        {
          "Expected": 15
        },
        {
          "Expected": 18
        },
        {
          "Expected": 27
        },
        {
          "Expected": 600
        },
        {
          "Expected": 1351
        }
      ]
JSONTests =  [
        {
          "array": [
            5,
            2,
            [
              7,
              -1
            ],
            3,
            [
              6,
              [
                -13,
                8
              ],
              4
            ]
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5
          ]
        },
        {
          "array": [
            1,
            2,
            [
              3
            ],
            4,
            5
          ]
        },
        {
          "array": [
            [
              1,
              2
            ],
            3,
            [
              4,
              5
            ]
          ]
        },
        {
          "array": [
            [
              [
                [
                  [
                    5
                  ]
                ]
              ]
            ]
          ]
        },
        {
          "array": [
            9,
            [
              2,
              -3,
              4
            ],
            1,
            [
              1,
              1,
              [
                1,
                1,
                1
              ]
            ],
            [
              [
                [
                  [
                    3,
                    4,
                    1
                  ]
                ]
              ],
              8
            ],
            [
              1,
              2,
              3,
              4,
              5,
              [
                6,
                7
              ],
              -7
            ],
            [
              1,
              [
                2,
                3,
                [
                  4,
                  5
                ]
              ],
              [
                6,
                0,
                [
                  7,
                  0,
                  -8
                ]
              ],
              -7
            ],
            [
              1,
              -3,
              2,
              [
                1,
                -3,
                2,
                [
                  1,
                  -3,
                  2
                ],
                [
                  1,
                  -3,
                  2,
                  [
                    1,
                    -3,
                    2
                  ]
                ],
                [
                  1,
                  -3,
                  2
                ]
              ]
            ],
            -3
          ]
        }
      ]

class ProductSumTests(unittest.TestCase):
    def test_product_sum(self):
        for i in range(0, len(JSONTests)):
            result = productSum(JSONTests[i]['array'])
            self.assertEqual(result, TestResults[i]['Expected'])