import unittest
from unittest import result
from solution import moveElementsToEnd

TestResults = [
    {
        "Expected": [
            4,
            1,
            3,
            2,
            2,
            2,
            2,
            2
        ]
    },
    {
        "Expected": []
    },
    {
        "Expected": [
            1,
            2,
            4,
            5,
            6
        ]
    },
    {
        "Expected": [
            3,
            3,
            3,
            3,
            3
        ]
    },
    {
        "Expected": [
            5,
            1,
            2,
            4,
            3
        ]
    },
    {
        "Expected": [
            1,
            2,
            4,
            5,
            3
        ]
    },
    {
        "Expected": [
            1,
            2,
            5,
            4,
            3
        ]
    },
    {
        "Expected": [
            6,
            4,
            5,
            2,
            2,
            2,
            2
        ]
    },
    {
        "Expected": [
            12,
            11,
            10,
            9,
            8,
            7,
            1,
            2,
            3,
            4,
            6,
            5,
            5,
            5,
            5,
            5,
            5
        ]
    },
    {
        "Expected": [
            1,
            2,
            3,
            4,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            5,
            5,
            5,
            5,
            5,
            5
        ]
    },
    {
        "Expected": [
            12,
            1,
            2,
            11,
            10,
            3,
            4,
            6,
            7,
            9,
            8,
            5,
            5,
            5,
            5,
            5,
            5
        ]
    }
]

JSONTests = [
    {
        "array": [
            2,
            1,
            2,
            2,
            2,
            3,
            4,
            2
        ],
        "toMove": 2
    },
    {
        "array": [],
        "toMove": 3
    },
    {
        "array": [
            1,
            2,
            4,
            5,
            6
        ],
        "toMove": 3
    },
    {
        "array": [
            3,
            3,
            3,
            3,
            3
        ],
        "toMove": 3
    },
    {
        "array": [
            3,
            1,
            2,
            4,
            5
        ],
        "toMove": 3
    },
    {
        "array": [
            1,
            2,
            4,
            5,
            3
        ],
        "toMove": 3
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            5
        ],
        "toMove": 3
    },
    {
        "array": [
            2,
            4,
            2,
            5,
            6,
            2,
            2
        ],
        "toMove": 2
    },
    {
        "array": [
            5,
            5,
            5,
            5,
            5,
            5,
            1,
            2,
            3,
            4,
            6,
            7,
            8,
            9,
            10,
            11,
            12
        ],
        "toMove": 5
    },
    {
        "array": [
            1,
            2,
            3,
            4,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            5,
            5,
            5,
            5,
            5,
            5
        ],
        "toMove": 5
    },
    {
        "array": [
            5,
            1,
            2,
            5,
            5,
            3,
            4,
            6,
            7,
            5,
            8,
            9,
            10,
            11,
            5,
            5,
            12
        ],
        "toMove": 5
    }
]


class MoveElementsToEndTests(unittest.TestCase):
    def test_move_elements_to_end(self):
        for i in range(0, len(JSONTests)):
            array = JSONTests[i]['array']
            toMove = JSONTests[i]['toMove']
            result = moveElementsToEnd(array, toMove)
            self.assertListEqual(result, TestResults[i]['Expected'])
