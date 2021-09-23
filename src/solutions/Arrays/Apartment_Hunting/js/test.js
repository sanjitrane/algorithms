const apartmentHunting = require('./solution')
const cases = require('../cases.json')

describe('Testing Apartment Hunting Algo', ()=>{
    test('Test if Function exists', ()=>{
        expect(typeof apartmentHunting).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            expect(apartmentHunting(item['blocks'], item['reqs'])).toEqual(TestResults[index]['Expected'])
        })
    })
})