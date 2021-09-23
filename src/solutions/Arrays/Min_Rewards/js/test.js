const minRewards = require('./solution')
const cases = require('../cases.json')

describe('Testing MinRewards Algo', ()=>{
    test('Test if function exists', ()=>{
        expect(typeof minRewards).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(minRewards(item['scores'])).toEqual(TestResults[index]['Expected'])
        })
    })
})