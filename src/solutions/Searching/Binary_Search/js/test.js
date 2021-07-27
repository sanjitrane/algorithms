const binarySearch = require('./solution')
const cases = require('../cases.json')

describe('Testing Binary Search Algo', ()=>{
  test('Binary Search function exists', ()=>{
    expect(typeof binarySearch).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {array, target} = item
      expect(binarySearch(array, target)).toEqual(TestResults[index]['Expected'])
    })
  })
})