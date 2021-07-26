const isPalindrome = require('./solution')
const cases = require('../cases.json')

describe('Testing Palindrome strings', ()=>{
  test('isPalindrome function exists',()=>{
    expect(typeof isPalindrome).toEqual('function')
  })

  const {TestResults, JSONTests} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {string} = item
      expect(isPalindrome(string)).toEqual(TestResults[index]['Expected'])
    })
  })
})