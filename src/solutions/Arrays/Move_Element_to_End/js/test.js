const moveElementToEnd = require('./solution')
const cases = require('../cases.json')

describe('Test moveElementToEnd', ()=>{
  test('moveElementToEnd function exists', ()=>{
    expect(typeof moveElementToEnd).toEqual('function')
  })

  const {JSONTests, TestResults} = cases 
  JSONTests.forEach((item, index)=>{
    const {array, toMove} = item
    test(`Test ${index}`, ()=>{
      expect(moveElementToEnd(array, toMove)).toEqual(TestResults[index]['Expected'])
    })
  })
})