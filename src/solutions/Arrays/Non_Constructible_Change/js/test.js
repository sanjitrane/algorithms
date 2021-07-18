const nonConstructibleChange = require('./solution')
const cases = require('../cases.json')

describe('Testing nonConstructibleChange function',()=>{
  test('nonConstructibleChange function exists',()=>{
    expect(typeof nonConstructibleChange).toEqual('function')
  })

  const {JSONTests, expectedOutput} = cases
  JSONTests.forEach((item,index)=>{
    test(`Test ${index}`,()=>{
      const {coins} = item
      expect(nonConstructibleChange(coins)).toEqual(expectedOutput[index])
    })
  })
})