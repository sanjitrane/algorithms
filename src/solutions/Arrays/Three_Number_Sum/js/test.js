const threeNumberSum = require('./solution')
const cases = require('../cases.json')

describe('Testing threeNumberSum', ()=>{
  test('threeNumberSum funnction exists', ()=>{
    expect(typeof threeNumberSum).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {array, targetSum} = item
      expect(threeNumberSum(array, targetSum)).toEqual(expect.arrayContaining(TestResults[index]["Expected"]))
    })
  })
})