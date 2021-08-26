const mergeIntervals = require('./solution')
const cases = require('../cases.json')

describe('Testing mergeInterval Algo', ()=>{
    test('MergeInterval function exists', ()=>{
        expect(typeof mergeIntervals).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            const {intervals} = item
            expect(mergeIntervals(intervals)).toEqual(TestResults[index]['Expected'])
        })
    })
})