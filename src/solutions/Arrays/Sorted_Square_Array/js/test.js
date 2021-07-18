const sortedSquareArray = require('./solution')
const cases = require('../cases.json')

describe('Testing sortedSquareArray function',()=>{
  test('Function is valid', ()=>{
    expect(typeof sortedSquareArray).toEqual('function')
  })

  
  const {jsonTests, expectedOutput} = cases
  
  jsonTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const array = item['array']
      const res = sortedSquareArray(array)
      expect(res).toEqual(expectedOutput[index])
    })
  })
})
