import unittest
from unittest import result
from solution import arrayOfProducts, arrayOfProducts1

TestResults = [
        {
          "Expected": [
            8,
            40,
            10,
            20
          ]
        },
        {
          "Expected": [
            384,
            48,
            64,
            192,
            96
          ]
        },
        {
          "Expected": [
            672,
            -1680,
            840,
            -240,
            560
          ]
        },
        {
          "Expected": [
            1620,
            4860,
            7290,
            14580,
            1620,
            2916,
            4860,
            7290
          ]
        },
        {
          "Expected": [
            4,
            4
          ]
        },
        {
          "Expected": [
            0,
            0,
            0,
            0
          ]
        },
        {
          "Expected": [
            1,
            1,
            1,
            1
          ]
        },
        {
          "Expected": [
            1,
            1,
            1
          ]
        },
        {
          "Expected": [
            -1,
            -1,
            -1,
            -1
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
            0,
            0,
            0,
            0,
            0
          ]
        },
        {
          "Expected": [
            362880,
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
        }
      ]
JSONTests = [
        {
          "array": [
            5,
            1,
            4,
            2
          ]
        },
        {
          "array": [
            1,
            8,
            6,
            2,
            4
          ]
        },
        {
          "array": [
            -5,
            2,
            -4,
            14,
            -6
          ]
        },
        {
          "array": [
            9,
            3,
            2,
            1,
            9,
            5,
            3,
            2
          ]
        },
        {
          "array": [
            4,
            4
          ]
        },
        {
          "array": [
            0,
            0,
            0,
            0
          ]
        },
        {
          "array": [
            1,
            1,
            1,
            1
          ]
        },
        {
          "array": [
            -1,
            -1,
            -1
          ]
        },
        {
          "array": [
            -1,
            -1,
            -1,
            -1
          ]
        },
        {
          "array": [
            0,
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
          ]
        },
        {
          "array": [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
          ]
        }
      ]

class ArrayOfProductsTests(unittest.TestCase):
	def test_array_of_products(self):
		for i in range(0,len(JSONTests)):
			array = JSONTests[i]['array']
			result = arrayOfProducts(array)
			self.assertEqual(result, TestResults[i]['Expected'])

	def test_array_of_products1(self):
		for i in range(0,len(JSONTests)):
			array = JSONTests[i]['array']
			result = arrayOfProducts1(array)
			self.assertEqual(result, TestResults[i]['Expected'])