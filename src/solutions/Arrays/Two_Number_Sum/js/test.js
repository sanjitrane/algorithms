const {twoNumberSum, twoNumberSum2 } = require('./solution.js')
const cases  = require('../cases.json')

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
