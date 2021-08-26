const longestPeak = require('./solution')
const cases = require('../cases.json')

describe('LongestPeak function Algo tests', ()=>{
    test('LongestPeak function exists', ()=>{
        expect(typeof longestPeak).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            const {array} = item
            expect(longestPeak(array)).toEqual(TestResults[index]['Expected'])
        })
    })
})