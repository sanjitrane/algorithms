const subarraySort = require('./solution')
const cases = require('../cases.json')

describe('Testing SubarraySort Algo', ()=>{
    test('Subarraysort function exists',()=>{
        expect(typeof subarraySort).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(subarraySort(item['array'])).toEqual(TestResults[index]['Expected'])
        })
    })
})