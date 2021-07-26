const isBalanced = require('./solution')
const cases = require('../cases.json')

describe('Testing Balanced Brackets function', ()=>{
  test('Balanced Bracket function exists', ()=>{
    expect(typeof isBalanced).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {string} = item
      expect(isBalanced(string)).toEqual(TestResults[index]['Expected'])
    })
  })
})