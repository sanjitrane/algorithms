const {twoNumberSum, twoNumberSum2 } = require('./solution.js')
const cases  = require('../cases.json')

// const jsonTests = [
//   {
//     "array": [
//       3,
//       5,
//       -4,
//       8,
//       11,
//       1,
//       -1,
//       6
//     ],
//     "targetSum": 10
//   },
//   {
//     "array": [
//       4,
//       6
//     ],
//     "targetSum": 10
//   },
//   {
//     "array": [
//       4,
//       6,
//       1
//     ],
//     "targetSum": 5
//   },
//   {
//     "array": [
//       4,
//       6,
//       1,
//       -3
//     ],
//     "targetSum": 3
//   },
//   {
//     "array": [
//       1,
//       2,
//       3,
//       4,
//       5,
//       6,
//       7,
//       8,
//       9
//     ],
//     "targetSum": 17
//   },
//   {
//     "array": [
//       1,
//       2,
//       3,
//       4,
//       5,
//       6,
//       7,
//       8,
//       9,
//       15
//     ],
//     "targetSum": 18
//   },
//   {
//     "array": [
//       -7,
//       -5,
//       -3,
//       -1,
//       0,
//       1,
//       3,
//       5,
//       7
//     ],
//     "targetSum": -5
//   },
//   {
//     "array": [
//       -21,
//       301,
//       12,
//       4,
//       65,
//       56,
//       210,
//       356,
//       9,
//       -47
//     ],
//     "targetSum": 163
//   },
//   {
//     "array": [
//       -21,
//       301,
//       12,
//       4,
//       65,
//       56,
//       210,
//       356,
//       9,
//       -47
//     ],
//     "targetSum": 164
//   },
//   {
//     "array": [
//       3,
//       5,
//       -4,
//       8,
//       11,
//       1,
//       -1,
//       6
//     ],
//     "targetSum": 15
//   },
//   {
//     "array": [
//       14
//     ],
//     "targetSum": 15
//   },
//   {
//     "array": [
//       15
//     ],
//     "targetSum": 15
//   }
// ]

// const expectedOutput = [
//   [11, -1],
//   [4,6],
//   [4,1],
//   [6,-3],
//   [8,9],
//   [3,15],
//   [-5,0],
//   [210,-47],
//   [],
//   [],
//   [],
//   []
// ]

describe('Checking function with multiple options',()=>{
  test('twoNumberSum function exists',()=>{
    expect(typeof twoNumberSum).toEqual('function');
  })

  cases.jsonTests.forEach((item, index)=>{
    test(`Test Case ${index + 1}`, ()=>{
      const array = cases.jsonTests[index]['array']
      const target = cases.jsonTests[index]['targetSum']
      const res = twoNumberSum(array, target)
      expect(res).toEqual(expect.arrayContaining(cases.expectedOutput[index]))
    })
  })
})

describe('Checking Solution 2 with multiple options',()=>{
  test('twoNumberSum2 function exists', ()=>{
    expect(typeof twoNumberSum2).toEqual('function')
  })

  cases.jsonTests.forEach((item, index)=>{
    test(`Test Case ${index}`,()=>{
      const array = cases.jsonTests[index]['array']
      const target = cases.jsonTests[index]['targetSum']
      const res = twoNumberSum2(array, target)
      expect(res).toEqual(expect.arrayContaining(cases.expectedOutput[index]))
    })
  })
})
