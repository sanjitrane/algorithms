import unittest
from solution import threeNumberSum

TestResults = [
    {
        "Expected": [
            [
                -8,
                2,
                6
            ],
            [
                -8,
                3,
                5
            ],
            [
                -6,
                1,
                5
            ]
        ]
    },
    {
        "Expected": [
            [
                1,
                2,
                3
            ]
        ]
    },
    {
        "Expected": []
    },
    {
        "Expected": [
            [
                -2,
                10,
                49
            ]
        ]
    },
    {
        "Expected": [
            [
                -8,
                3,
                5
            ],
            [
                -6,
                1,
                5
            ],
            [
                -1,
                0,
                1
            ]
        ]
    },
    {
        "Expected": [
            [
                -8,
                2,
                6
            ],
            [
                -8,
                3,
                5
            ],
            [
                -6,
                0,
                6
            ],
            [
                -6,
                1,
                5
            ],
            [
                -1,
                0,
                1
            ]
        ]
    },
    {
        "Expected": [
            [
                -8,
                2,
                6
            ],
            [
                -8,
                3,
                5
            ],
            [
                -6,
                0,
                6
            ],
            [
                -6,
                1,
                5
            ],
            [
                -5,
                -1,
                6
            ],
            [
                -5,
                0,
                5
            ],
            [
                -5,
                2,
                3
            ],
            [
                -1,
                0,
                1
            ]
        ]
    },
    {
        "Expected": [
            [
                1,
                2,
                15
            ],
            [
                1,
                8,
                9
            ],
            [
                2,
                7,
                9
            ],
            [
                3,
                6,
                9
            ],
            [
                3,
                7,
                8
            ],
            [
                4,
                5,
                9
            ],
            [
                4,
                6,
                8
            ],
            [
                5,
                6,
                7
            ]
        ]
    },
    {
        "Expected": [
            [
                8,
                9,
                15
            ]
        ]
    },
    {
        "Expected": []
    },
    {
        "Expected": []
    }
]
JSONTests = [
    {
        "array": [
            12,
            3,
            1,
            2,
            -6,
            5,
            -8,
            6
        ],
        "targetSum": 0
    },
    {
        "array": [
            1,
            2,
            3
        ],
        "targetSum": 6
    },
    {
        "array": [
            1,
            2,
            3
        ],
        "targetSum": 7
    },
    {
        "array": [
            8,
            10,
            -2,
            49,
            14
        ],
        "targetSum": 57
    },
    {
        "array": [
            12,
            3,
            1,
            2,
            -6,
            5,
            0,
            -8,
            -1
        ],
        "targetSum": 0
    },
    {
        "array": [
            12,
            3,
            1,
            2,
            -6,
            5,
            0,
            -8,
            -1,
            6
        ],
        "targetSum": 0
    },
    {
        "array": [
            12,
            3,
            1,
            2,
            -6,
            5,
            0,
            -8,
            -1,
            6,
            -5
        ],
        "targetSum": 0
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            15
        ],
        "targetSum": 18
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            15
        ],
        "targetSum": 32
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            15
        ],
        "targetSum": 33
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            15
        ],
        "targetSum": 5
    }
]


class ThreeNumberSumTests(unittest.TestCase):
    def test_three_number_sum(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            targetSum = JSONTests[i]['targetSum']
            result = threeNumberSum(array, targetSum)
            print(result, TestResults[i]['Expected'])
            self.assertEqual(result, TestResults[i]['Expected'])
