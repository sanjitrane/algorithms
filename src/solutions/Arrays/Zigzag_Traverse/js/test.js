const zigzagTraverse = require('./solution')
const cases = require('../cases.json')

describe('Testing zigzag traverse Algo', ()=>{
    test('Test if the function exists', ()=>{
        expect(typeof zigzagTraverse).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(zigzagTraverse(item['array'])).toEqual(TestResults[index]['Expected'])
        })
    })
})