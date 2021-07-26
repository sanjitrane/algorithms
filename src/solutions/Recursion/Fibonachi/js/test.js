const {fib, fib1} = require('./solution')
const cases = require('../cases.json')

describe('Testing Fibonachi algo', ()=>{
  test('Fibonachi function',()=>{
    expect(typeof fib).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const n = item['n']
      expect(fib(n)).toEqual(TestResults[index]['Expected'])
    })
  })

  test('Fibonachi1 function',()=>{
    expect(typeof fib1).toEqual('function')
  })

  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const n = item['n']
      expect(fib1(n)).toEqual(TestResults[index]['Expected'])
    })
  })
})