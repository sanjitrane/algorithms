const firstDuplicateValue = require('./solution')
const cases = require('../cases.json')

describe('Testing FirstDuplicateValue Algo', ()=>{
    test('Test if firstDuplicateValue exists', ()=>{
        expect(typeof firstDuplicateValue).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            const {array} = item
            expect(firstDuplicateValue(array)).toEqual(TestResults[index]['Expected'])
        })
    })
})
