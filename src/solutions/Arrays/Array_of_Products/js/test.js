const {arrayOfProducts, arrayOfProducts1} = require('./solution')
const cases = require('../cases.json')

describe('Testing Array of Products Algo', ()=>{
    test('arrayOfProducts function exists', ()=>{
        expect(typeof arrayOfProducts).toEqual('function')
        expect(typeof arrayOfProducts1).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        
        test(`Test ${index}`,()=>{
            const {array} = item
            const expected = TestResults[index]['Expected']
            expect(arrayOfProducts(array)).toEqual(expected)
        })

        test(`Test ${index}`,()=>{
            const {array} = item
            const expected = TestResults[index]['Expected']
            expect(arrayOfProducts1(array)).toEqual(expected)
        })
    })   
})