const minNumberOfCoinsForChange = require('./solution')
const cases = require('../cases.json')

describe('Testing MinNumberOfCoinsForChange Algo', ()=>{
    test('Test if the function exists', ()=>{
        expect(typeof minNumberOfCoinsForChange).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        const {n, denoms} = item
        test('Passed params are of required data-types', ()=>{
            expect(typeof n).toBe('number')
            expect(Array.isArray(denoms)).toBe(true)
        })
        test(`Test ${index}`,()=>{
            expect(minNumberOfCoinsForChange(n, denoms)).toEqual(TestResults[index]['Expected'])
        })
    })
})