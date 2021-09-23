const longestRange = require('./solution')
const cases = require('../cases.json')

describe('Testing LongestRange Algo', ()=>{
    test('Test if function exists', ()=>{
        expect(typeof longestRange).toEqual('function')
    })
    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`,()=>{
            expect(longestRange(item['array'])).toEqual(TestResults[index]['Expected'])
        })
    })
})