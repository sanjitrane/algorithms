const classPhoto = require('./solution')
const cases = require('../cases.json')

describe('Testing ClassPhoto Algo', ()=>{
  test('ClassPhoto function exists', ()=>{
    expect(typeof classPhoto).toEqual('function')
  })

  const {TestResults, JSONTests} = cases
  JSONTests.forEach((item, index)=>{
    test(`Test ${index}`, ()=>{
      const {redShirtHeights, blueShirtHeights} = item
      expect(classPhoto(redShirtHeights, blueShirtHeights)).toEqual(TestResults[index]['Expected'])
    }) 
  }) 
})