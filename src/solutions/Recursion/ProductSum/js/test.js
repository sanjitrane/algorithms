const productSum = require('./solution')
const cases = require('../cases.json')

describe('Testing ProductSum Algo',()=>{
    test('ProductSum function exists', ()=>{
        expect(typeof productSum).toEqual('function')
    })
    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(productSum(item['array'])).toEqual(TestResults[index]['Expected'])
        })
    })
})