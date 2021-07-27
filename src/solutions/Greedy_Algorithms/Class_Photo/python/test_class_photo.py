import unittest
from unittest import result
from solution import classPhoto

TestResults = [
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    }
]
JSONTests = [
    {
        "blueShirtHeights": [
            6,
            9,
            2,
            4,
            5
        ],
        "redShirtHeights": [
            5,
            8,
            1,
            3,
            4
        ]
    },
    {
        "blueShirtHeights": [
            5,
            8,
            1,
            3,
            4
        ],
        "redShirtHeights": [
            6,
            9,
            2,
            4,
            5
        ]
    },
    {
        "blueShirtHeights": [
            5,
            8,
            1,
            3,
            4,
            9
        ],
        "redShirtHeights": [
            6,
            9,
            2,
            4,
            5,
            1
        ]
    },
    {
        "blueShirtHeights": [
            6
        ],
        "redShirtHeights": [
            6
        ]
    },
    {
        "blueShirtHeights": [
            125
        ],
        "redShirtHeights": [
            126
        ]
    },
    {
        "blueShirtHeights": [
            2,
            3,
            4,
            5,
            6
        ],
        "redShirtHeights": [
            1,
            2,
            3,
            4,
            5
        ]
    },
    {
        "blueShirtHeights": [
            5,
            6,
            7,
            2,
            3,
            1,
            2,
            3
        ],
        "redShirtHeights": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "blueShirtHeights": [
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2
        ],
        "redShirtHeights": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "blueShirtHeights": [
            126
        ],
        "redShirtHeights": [
            125
        ]
    },
    {
        "blueShirtHeights": [
            21,
            5,
            4,
            4,
            4,
            4,
            4,
            4,
            4
        ],
        "redShirtHeights": [
            19,
            2,
            4,
            6,
            2,
            3,
            1,
            1,
            4
        ]
    },
    {
        "blueShirtHeights": [
            20,
            5,
            4,
            4,
            4,
            4,
            4,
            4
        ],
        "redShirtHeights": [
            19,
            19,
            21,
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "blueShirtHeights": [
            2,
            4,
            7,
            5,
            1
        ],
        "redShirtHeights": [
            3,
            5,
            6,
            8,
            2
        ]
    },
    {
        "blueShirtHeights": [
            2,
            4,
            7,
            5,
            1,
            6
        ],
        "redShirtHeights": [
            3,
            5,
            6,
            8,
            2,
            1
        ]
    },
    {
        "blueShirtHeights": [
            5,
            4
        ],
        "redShirtHeights": [
            4,
            5
        ]
    },
    {
        "blueShirtHeights": [
            5,
            4
        ],
        "redShirtHeights": [
            5,
            6
        ]
    }
]


class ClassPhotooTests(unittest.TestCase):
    def test_class_photo(self):
        for i in range(0, len(JSONTests)):
            redShirtHeights = JSONTests[i]['redShirtHeights']
            blueShirtHeights = JSONTests[i]['blueShirtHeights']
            result = classPhoto(redShirtHeights, blueShirtHeights)
            self.assertEqual(result, TestResults[i]['Expected'])
