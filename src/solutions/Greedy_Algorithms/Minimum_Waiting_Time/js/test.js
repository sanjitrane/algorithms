const minimumWaitingTime = require('./solution')
const cases  = require('../cases.json') 

describe('Testing MinimumWaitingTime Algo',()=>{
  test('MininumWaitingTime function exists', ()=>{
    expect(typeof minimumWaitingTime).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {queries} = item
      expect(minimumWaitingTime(queries)).toEqual(TestResults[index]['Expected'])
    })
  })
})