import unittest
from solution import waterfallStreams

TestResults = [
        {
          "Expected": [
            0,
            0,
            0,
            25,
            25,
            0,
            0
          ]
        },
        {
          "Expected": [
            100
          ]
        },
        {
          "Expected": [
            0
          ]
        },
        {
          "Expected": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        },
        {
          "Expected": [
            0,
            0,
            0,
            0,
            25,
            0,
            0
          ]
        },
        {
          "Expected": [
            25,
            6.25,
            0,
            0,
            0,
            6.25,
            0
          ]
        },
        {
          "Expected": [
            0,
            0,
            0,
            0,
            0,
            0,
            0
          ]
        },
        {
          "Expected": [
            25,
            0,
            12.5,
            0,
            4.6875,
            0,
            0,
            0,
            0,
            7.8125,
            0,
            0,
            3.125,
            37.5
          ]
        },
        {
          "Expected": [
            25,
            0,
            12.5,
            0,
            0,
            0,
            12.5,
            6.25,
            0,
            3.125,
            0,
            0,
            3.125,
            37.5
          ]
        }
      ]
JSONTests = [
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              1,
              1,
              0,
              0,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              1
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 3
        },
        {
          "array": [
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ]
          ],
          "source": 0
        },
        {
          "array": [
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              0
            ],
            [
              1
            ],
            [
              0
            ]
          ],
          "source": 0
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              0,
              1,
              0,
              1,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              1,
              1,
              0,
              0,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              1
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 3
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              0,
              1,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              1,
              1,
              0,
              0,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              1
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 3
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              1,
              0,
              0,
              0,
              1
            ],
            [
              0,
              0,
              1,
              0,
              1,
              1,
              0
            ],
            [
              0,
              1,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              1,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              0,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 3
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              1,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              1,
              0,
              0,
              0,
              1
            ],
            [
              0,
              0,
              1,
              0,
              1,
              1,
              0
            ],
            [
              0,
              1,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              1,
              0,
              0,
              0
            ],
            [
              1,
              1,
              1,
              1,
              1,
              1,
              1
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 6
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              1,
              1,
              1,
              0,
              0,
              0,
              0,
              0,
              0,
              1,
              1,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              1,
              1,
              1,
              0,
              0,
              1,
              1,
              1,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              1,
              0,
              0,
              0,
              0,
              1,
              1,
              0,
              0,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              1,
              0,
              0,
              1,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 8
        },
        {
          "array": [
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              1,
              1,
              1,
              1,
              0,
              0,
              0,
              0,
              1,
              1,
              1,
              1,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              1,
              1,
              1,
              0,
              0,
              1,
              1,
              1,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              1,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              1,
              1,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              1,
              0,
              0,
              1,
              0,
              0,
              0,
              0,
              0
            ],
            [
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0
            ]
          ],
          "source": 8
        }
]

class WaterfallStreamsTests(unittest.TestCase):
    def test_waterfall_streams(self):
        for i in range(0, len(JSONTests)):
            result = waterfallStreams(JSONTests[i]['array'], JSONTests[i]['source'])
            self.assertEqual(result, TestResults[i]['Expected'])