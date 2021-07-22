const spiralTraverse = require('./solution')
const cases = require('../cases.json')

describe('Testing spiralTraverse fuction', ()=>{
  test('spiralTraverse function exists', ()=>{
    expect(typeof spiralTraverse).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {array} = item
      expect(spiralTraverse(array)).toEqual(TestResults[index]['Expected'])
    })
  })
})