const smallestDifference = require('./solution')
const cases = require('../cases.json')

describe('Testing smallestDifference function', ()=>{
  test('smallestDifference function exists', ()=>{
    expect(typeof smallestDifference).toEqual('function')
  })

  const {TestResults, JSONTests} = cases 
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`,()=>{
      const {arrayOne, arrayTwo} = item 
      expect(smallestDifference(arrayOne, arrayTwo)).toEqual(expect.arrayContaining(TestResults[index]["Expected"]))
    })
  })
})