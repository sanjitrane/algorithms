const threeLargestNums = require('./solution')
const cases = require('../cases.json')

describe('Testing Three Largest Numbers Algo', ()=>{
  test('threeLargestSum function exists', ()=>{
    expect(typeof threeLargestNums).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {array} = item
      expect(threeLargestNums(array)).toEqual(TestResults[index]['Expected'])
    })
  })
})