import unittest
from solution import apartmentHunting

TestResults = [
        {
          "Expected": 3
        },
        {
          "Expected": 2
        },
        {
          "Expected": 2
        },
        {
          "Expected": 4
        },
        {
          "Expected": 2
        },
        {
          "Expected": 7
        },
        {
          "Expected": 4
        }
      ]
JSONTests =  [
        {
          "blocks": [
            {
              "gym": False,
              "school": True,
              "store": False
            },
            {
              "gym": True,
              "school": False,
              "store": False
            },
            {
              "gym": True,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "school": True,
              "store": True
            }
          ],
          "reqs": [
            "gym",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "gym": False,
              "office": True,
              "school": True,
              "store": False
            },
            {
              "gym": True,
              "office": False,
              "school": False,
              "store": False
            },
            {
              "gym": True,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "school": True,
              "store": True
            }
          ],
          "reqs": [
            "gym",
            "office",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "gym": False,
              "office": True,
              "school": True,
              "store": False
            },
            {
              "gym": True,
              "office": False,
              "school": False,
              "store": False
            },
            {
              "gym": True,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "school": True,
              "store": True
            }
          ],
          "reqs": [
            "gym",
            "office",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "foo": True,
              "gym": False,
              "kappa": False,
              "office": True,
              "school": True,
              "store": False
            },
            {
              "foo": True,
              "gym": True,
              "kappa": False,
              "office": False,
              "school": False,
              "store": False
            },
            {
              "foo": True,
              "gym": True,
              "kappa": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "foo": True,
              "gym": False,
              "kappa": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "foo": True,
              "gym": True,
              "kappa": False,
              "office": False,
              "school": True,
              "store": False
            },
            {
              "foo": True,
              "gym": False,
              "kappa": False,
              "office": False,
              "school": True,
              "store": True
            }
          ],
          "reqs": [
            "gym",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "gym": True,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": True
            },
            {
              "gym": True,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "school": True,
              "store": False
            }
          ],
          "reqs": [
            "gym",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "gym": True,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": True
            },
            {
              "gym": True,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "pool": True,
              "school": False,
              "store": False
            }
          ],
          "reqs": [
            "gym",
            "pool",
            "school",
            "store"
          ]
        },
        {
          "blocks": [
            {
              "gym": True,
              "office": False,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": True,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": True,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": False,
              "school": False,
              "store": True
            },
            {
              "gym": True,
              "office": True,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": True,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": False,
              "school": False,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": False,
              "school": True,
              "store": False
            },
            {
              "gym": False,
              "office": False,
              "pool": True,
              "school": False,
              "store": False
            }
          ],
          "reqs": [
            "gym",
            "pool",
            "school",
            "store"
          ]
        }
      ]

class ApartmentHuntingTests(unittest.TestCase):
    def test_apartment_hunting(self):
        for i in range(0, len(JSONTests)):
            result = apartmentHunting(JSONTests[i]['blocks'], JSONTests[i]['reqs'])
            self.assertEqual(result, TestResults[i]['Expected'])