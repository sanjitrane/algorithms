import unittest
from solution import subArraySort
TestResults = [
        {
          "Expected": [
            3,
            9
          ]
        },
        {
          "Expected": [
            -1,
            -1
          ]
        },
        {
          "Expected": [
            0,
            1
          ]
        },
        {
          "Expected": [
            4,
            9
          ]
        },
        {
          "Expected": [
            4,
            6
          ]
        },
        {
          "Expected": [
            2,
            4
          ]
        },
        {
          "Expected": [
            0,
            12
          ]
        },
        {
          "Expected": [
            0,
            11
          ]
        },
        {
          "Expected": [
            1,
            11
          ]
        },
        {
          "Expected": [
            1,
            12
          ]
        },
        {
          "Expected": [
            6,
            7
          ]
        },
        {
          "Expected": [
            6,
            16
          ]
        },
        {
          "Expected": [
            4,
            24
          ]
        },
        {
          "Expected": [
            2,
            19
          ]
        },
        {
          "Expected": [
            2,
            19
          ]
        },
        {
          "Expected": [
            -1,
            -1
          ]
        },
        {
          "Expected": [
            -1,
            -1
          ]
        }
      ]
JSONTests = [
        {
          "array": [
            1,
            2,
            4,
            7,
            10,
            11,
            7,
            12,
            6,
            7,
            16,
            18,
            19
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
            2,
            1
          ]
        },
        {
          "array": [
            1,
            2,
            4,
            7,
            10,
            11,
            7,
            12,
            7,
            7,
            16,
            18,
            19
          ]
        },
        {
          "array": [
            1,
            2,
            4,
            7,
            10,
            11,
            7,
            12,
            13,
            14,
            16,
            18,
            19
          ]
        },
        {
          "array": [
            1,
            2,
            8,
            4,
            5
          ]
        },
        {
          "array": [
            4,
            8,
            7,
            12,
            11,
            9,
            -1,
            3,
            9,
            16,
            -15,
            51,
            7
          ]
        },
        {
          "array": [
            4,
            8,
            7,
            12,
            11,
            9,
            -1,
            3,
            9,
            16,
            -15,
            11,
            57
          ]
        },
        {
          "array": [
            -41,
            8,
            7,
            12,
            11,
            9,
            -1,
            3,
            9,
            16,
            -15,
            11,
            57
          ]
        },
        {
          "array": [
            -41,
            8,
            7,
            12,
            11,
            9,
            -1,
            3,
            9,
            16,
            -15,
            51,
            7
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            8,
            7,
            9,
            10,
            11
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            18,
            7,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            19
          ]
        },
        {
          "array": [
            1,
            2,
            3,
            4,
            5,
            6,
            18,
            21,
            22,
            7,
            14,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            19,
            4,
            14,
            11,
            6,
            33,
            35,
            41,
            55
          ]
        },
        {
          "array": [
            1,
            2,
            20,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19
          ]
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
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            2
          ]
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
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20
          ]
        },
        {
          "array": [
            0,
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89
          ]
        }
      ]

class SubArraySortTests(unittest.TestCase):
    def test_sub_array_sort(self):
        for i in range(0, len(JSONTests)):
            result = subArraySort(JSONTests[i]['array'])
            self.assertEqual(result, TestResults[i]['Expected'])