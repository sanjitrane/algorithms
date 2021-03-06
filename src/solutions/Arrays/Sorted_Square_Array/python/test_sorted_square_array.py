import unittest
from unittest import result
from solution import sortedSquareArray

jsonTests = [
    {
        "array": [
            1,
            2,
            3,
            5,
            6,
            8,
            9
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
            3,
            4,
            5
        ]
    },
    {
        "array": [
            0
        ]
    },
    {
        "array": [
            10
        ]
    },
    {
        "array": [
            -1
        ]
    },
    {
        "array": [
            -2,
            -1
        ]
    },
    {
        "array": [
            -5,
            -4,
            -3,
            -2,
            -1
        ]
    },
    {
        "array": [
            -10
        ]
    },
    {
        "array": [
            -10,
            -5,
            0,
            5,
            10
        ]
    },
    {
        "array": [
            -7,
            -3,
            1,
            9,
            22,
            30
        ]
    },
    {
        "array": [
            -50,
            -13,
            -2,
            -1,
            0,
            0,
            1,
            1,
            2,
            3,
            19,
            20
        ]
    },
    {
        "array": [
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
    },
    {
        "array": [
            -1,
            -1,
            2,
            3,
            3,
            3,
            4
        ]
    },
    {
        "array": [
            -3,
            -2,
            -1
        ]
    },
    {
        "array": [
            -3,
            -2,
            -1
        ]
    }
]

expectedOutput = [
    [
        1,
        4,
        9,
        25,
        36,
        64,
        81
    ],
    [
        1
    ],
    [
        1,
        4
    ],
    [
        1,
        4,
        9,
        16,
        25
    ],
    [
        0
    ],
    [
        100
    ],
    [
        1
    ],
    [
        1,
        4
    ],
    [
        1,
        4,
        9,
        16,
        25
    ],
    [
        100
    ],
    [
        0,
        25,
        25,
        100,
        100
    ],
    [
        1,
        9,
        49,
        81,
        484,
        900
    ],
    [
        0,
        0,
        1,
        1,
        1,
        4,
        4,
        9,
        169,
        361,
        400,
        2500
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
        0
    ],
    [
        1,
        1,
        4,
        9,
        9,
        9,
        16
    ],
    [
        1,
        4,
        9
    ],
    [
        1,
        4,
        9
    ]
]


class SortedSquareArrayTests(unittest.TestCase):
    def test_sortedSquareArray(self):
        for item in range(0, len(jsonTests)):
            array = jsonTests[item]["array"]
            result = sortedSquareArray(array)
            testValue = set(result) == set(expectedOutput[item])
            self.assertTrue(testValue)
