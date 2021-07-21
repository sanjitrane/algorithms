const {monotonicArray, isMonotonic} = require('./solution')
const cases = require('../cases.json')

describe('Testing MonotonicArray algo', ()=>{
  test(`MonotonicArray exists`, ()=>{
    expect(typeof monotonicArray).toEqual('function')
  })
  
  const {TestResults, JSONTests} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`,()=>{
      const {array} = item
      expect(monotonicArray(array)).toEqual(TestResults[index]['Expected'])
    })
  })

  test(`isMonotonic exists`, ()=>{
    expect(typeof isMonotonic).toEqual('function')
  })
  
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`,()=>{
      const {array} = item
      expect(isMonotonic(array)).toEqual(TestResults[index]['Expected'])
    })
  })
})