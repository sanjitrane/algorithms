import unittest
from unittest import result
from solution import tournamentWinner

JSONTests = [
    {
        "competitions": [
            [
                "HTML",
                "C#"
            ],
            [
                "C#",
                "Python"
            ],
            [
                "Python",
                "HTML"
            ]
        ],
        "results": [
            0,
            0,
            1
        ]
    },
    {
        "competitions": [
            [
                "HTML",
                "Java"
            ],
            [
                "Java",
                "Python"
            ],
            [
                "Python",
                "HTML"
            ]
        ],
        "results": [
            0,
            1,
            1
        ]
    },
    {
        "competitions": [
            [
                "HTML",
                "Java"
            ],
            [
                "Java",
                "Python"
            ],
            [
                "Python",
                "HTML"
            ],
            [
                "C#",
                "Python"
            ],
            [
                "Java",
                "C#"
            ],
            [
                "C#",
                "HTML"
            ]
        ],
        "results": [
            0,
            1,
            1,
            1,
            0,
            1
        ]
    },
    {
        "competitions": [
            [
                "HTML",
                "Java"
            ],
            [
                "Java",
                "Python"
            ],
            [
                "Python",
                "HTML"
            ],
            [
                "C#",
                "Python"
            ],
            [
                "Java",
                "C#"
            ],
            [
                "C#",
                "HTML"
            ],
            [
                "SQL",
                "C#"
            ],
            [
                "HTML",
                "SQL"
            ],
            [
                "SQL",
                "Python"
            ],
            [
                "SQL",
                "Java"
            ]
        ],
        "results": [
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            1,
            1,
            0
        ]
    },
    {
        "competitions": [
            [
                "Bulls",
                "Eagles"
            ]
        ],
        "results": [
            1
        ]
    },
    {
        "competitions": [
            [
                "Bulls",
                "Eagles"
            ],
            [
                "Bulls",
                "Bears"
            ],
            [
                "Bears",
                "Eagles"
            ]
        ],
        "results": [
            0,
            0,
            0
        ]
    },
    {
        "competitions": [
            [
                "Bulls",
                "Eagles"
            ],
            [
                "Bulls",
                "Bears"
            ],
            [
                "Bulls",
                "Monkeys"
            ],
            [
                "Eagles",
                "Bears"
            ],
            [
                "Eagles",
                "Monkeys"
            ],
            [
                "Bears",
                "Monkeys"
            ]
        ],
        "results": [
            1,
            1,
            1,
            1,
            1,
            1
        ]
    },
    {
        "competitions": [
            [
                "AlgoMasters",
                "FrontPage Freebirds"
            ],
            [
                "Runtime Terror",
                "Static Startup"
            ],
            [
                "WeC#",
                "Hypertext Assassins"
            ],
            [
                "AlgoMasters",
                "WeC#"
            ],
            [
                "Static Startup",
                "Hypertext Assassins"
            ],
            [
                "Runtime Terror",
                "FrontPage Freebirds"
            ],
            [
                "AlgoMasters",
                "Runtime Terror"
            ],
            [
                "Hypertext Assassins",
                "FrontPage Freebirds"
            ],
            [
                "Static Startup",
                "WeC#"
            ],
            [
                "AlgoMasters",
                "Static Startup"
            ],
            [
                "FrontPage Freebirds",
                "WeC#"
            ],
            [
                "Hypertext Assassins",
                "Runtime Terror"
            ],
            [
                "AlgoMasters",
                "Hypertext Assassins"
            ],
            [
                "WeC#",
                "Runtime Terror"
            ],
            [
                "FrontPage Freebirds",
                "Static Startup"
            ]
        ],
        "results": [
            1,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0
        ]
    },
    {
        "competitions": [
            [
                "HTML",
                "Java"
            ],
            [
                "Java",
                "Python"
            ],
            [
                "Python",
                "HTML"
            ],
            [
                "C#",
                "Python"
            ],
            [
                "Java",
                "C#"
            ],
            [
                "C#",
                "HTML"
            ],
            [
                "SQL",
                "C#"
            ],
            [
                "HTML",
                "SQL"
            ],
            [
                "SQL",
                "Python"
            ],
            [
                "SQL",
                "Java"
            ]
        ],
        "results": [
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            1,
            1
        ]
    },
    {
        "competitions": [
            [
                "A",
                "B"
            ]
        ],
        "results": [
            0
        ]
    }
]

expectedOutput = [
    "Python",
    "Java",
    "C#",
    "C#",
    "Bulls",
    "Eagles",
    "Bulls",
    "AlgoMasters",
    "SQL",
    "B"
]


class TournamentWinnerTests(unittest.TestCase):
    def test_tournamentWinner(self):
        for i in range(0, len(JSONTests)):
            competitions = JSONTests[i]['competitions']
            results = JSONTests[i]['results']
            result = tournamentWinner(competitions, results)
            self.assertEqual(result, expectedOutput[i])
