const fourNumberSum = require('./solution')
const cases = require('../cases.json')

describe('FourNumberSum Algo test',()=>{
    test('Four Number Sum function exists', ()=>{
        expect(typeof fourNumberSum).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(fourNumberSum(item['array'], item['targetSum'])).toEqual(TestResults[index]['Expected'])
        })
    })
})