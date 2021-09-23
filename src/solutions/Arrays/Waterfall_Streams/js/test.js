const waterfallStreams = require('./solution')
const cases = require('../cases.json')

describe('Testing Waterfall Stream Algo', ()=>{
    test('Test if function exists', ()=>{
        expect(typeof waterfallStreams).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        const {array, source} = item
        test(`Test ${index}`,()=>{
            expect(waterfallStreams(array, source)).toEqual(TestResults[index]['Expected'])
        })
    })
})