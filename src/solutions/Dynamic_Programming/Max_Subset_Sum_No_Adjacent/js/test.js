const maxSubsetSumNoAdjacent = require('./solution')
const cases = require('../cases.json')

describe('Testing MaxSubsetSumNoAdjacent Algo', ()=>{
    test('Test if function exists', ()=>{
        expect(typeof maxSubsetSumNoAdjacent).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        const array = item['array']
        test('Passed argument is an array', ()=>{
            expect(Array.isArray(array)).toBe(true)
        })
        test(`Test ${index}`, ()=>{
            expect(maxSubsetSumNoAdjacent(array)).toEqual(TestResults[index]['Expected'])
        })
    })
})