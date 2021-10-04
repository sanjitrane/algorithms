const numberOfWaysToMakeChange = require('./solution')
const cases = require('../cases.json')

describe('Testing NumberOfWaysToMakeChange Algo', ()=>{
    test('Test if the function exists', ()=>{
        expect(typeof numberOfWaysToMakeChange).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        const {n, denoms} = item
        test('passed params are of right data-type', ()=>{
            expect(typeof n).toBe('number')
            expect(Array.isArray(denoms)).toBe(true)
        })

        test(`Test ${index}`, ()=>{
            expect(numberOfWaysToMakeChange(n, denoms)).toEqual(TestResults[index]['Expected'])
        })

    })
})