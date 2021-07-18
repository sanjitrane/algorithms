import unittest
from solution import isValidateSubsequence

jsonTests = [
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            -1,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            22,
            25,
            6
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            25
        ]
    },
    {
        "array": [
            1,
            1,
            1,
            1,
            1
        ],
        "sequence": [
            1,
            1,
            1
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10,
            12
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            4,
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            23,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            22,
            25,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            22,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            -1,
            -1
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            -1,
            -1,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            -1,
            -2
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            26
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            25,
            22,
            6,
            -1,
            8,
            10
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            26,
            22,
            8
        ]
    },
    {
        "array": [
            1,
            1,
            6,
            1
        ],
        "sequence": [
            1,
            1,
            1,
            6
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            1,
            6,
            -1,
            10,
            11,
            11,
            11,
            11
        ]
    },
    {
        "array": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10
        ],
        "sequence": [
            5,
            1,
            22,
            25,
            6,
            -1,
            8,
            10,
            10
        ]
    }
]

expectedOutput = [True, True, True, True, True, True, True, True, True, False, False,
                  False, False, False, False, False, False, False, False, False, False, False, False]


class validateSubsequenceTest(unittest.TestCase):
    def test_validate_sequence(self):
        for i in range(0, len(jsonTests)):
            array = jsonTests[i]['array']
            sequence = jsonTests[i]['sequence']
            result = isValidateSubsequence(array, sequence)
            self.assertTrue(result == expectedOutput[i])
