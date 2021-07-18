
  const algos = [
    {
      "category": "Arrays",
      "title": "Two Number Sum",
      "difficulty": "green",
      "desc": "Write a function that takes in a non-empty array of distinct integers and an\n  integer representing a target sum. If any two numbers in the input array sum\n  up to the target sum, the function should return them in an array, in any\n  order. If no two numbers sum up to the target sum, the function should return\n  an empty array.\n\u003c/p\u003e\n\u003cp\u003e\n  Note that the target sum has to be obtained by summing two different integers\n  in the array; you can't add a single integer to itself in order to obtain the\n  target sum.\n\u003c/p\u003e\n\u003cp\u003e\n  You can assume that there will be at most one pair of numbers summing up to\n  the target sum.\n\u003c/p\u003e\n\u003ch3\u003eSample Input\u003c/h3\u003e\n\u003cpre\u003e\n\u003cspan class=\"CodeEditor-promptParameter\"\u003earray\u003c/span\u003e = [3, 5, -4, 8, 11, 1, -1, 6]\n\u003cspan class=\"CodeEditor-promptParameter\"\u003etargetSum\u003c/span\u003e = 10\n\u003c/pre\u003e\n\u003ch3\u003eSample Output\u003c/h3\u003e\n\u003cpre\u003e\n[-1, 11] \u003cspan class=\"CodeEditor-promptComment\"\u003e// the numbers could be in reverse order",
      "hints": [
        "Try using two for loops to sum all possible pairs of numbers in the input array. What are the time and space implications of this approach?",
        "Realize that for every number X in the input array, you are essentially trying to find a corresponding number Y such that X + Y = targetSum. With two variables in this equation known to you, it shouldn't be hard to solve for Y.",
        "Try storing every number in a hash table, solving the equation mentioned in Hint #2 for every number, and checking if the Y that you find is stored in the hash table. What are the time and space implications of this approach?"
      ],
      "spaceTime": "O(n) time | O(n) space - where n is the length of the input array",
      "jsonTests": [
        {
          "array": [
            3,
            5,
            -4,
            8,
            11,
            1,
            -1,
            6
          ],
          "targetSum": 10
        },
        {
          "array": [
            4,
            6
          ],
          "targetSum": 10
        },
        {
          "array": [
            4,
            6,
            1
          ],
          "targetSum": 5
        },
        {
          "array": [
            4,
            6,
            1,
            -3
          ],
          "targetSum": 3
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
            9
          ],
          "targetSum": 17
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
            -7,
            -5,
            -3,
            -1,
            0,
            1,
            3,
            5,
            7
          ],
          "targetSum": -5
        },
        {
          "array": [
            -21,
            301,
            12,
            4,
            65,
            56,
            210,
            356,
            9,
            -47
          ],
          "targetSum": 163
        },
        {
          "array": [
            -21,
            301,
            12,
            4,
            65,
            56,
            210,
            356,
            9,
            -47
          ],
          "targetSum": 164
        },
        {
          "array": [
            3,
            5,
            -4,
            8,
            11,
            1,
            -1,
            6
          ],
          "targetSum": 15
        },
        {
          "array": [
            14
          ],
          "targetSum": 15
        },
        {
          "array": [
            15
          ],
          "targetSum": 15
        }
      ],
    }
  ]
