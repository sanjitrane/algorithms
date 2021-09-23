const calendarMatching = require('./solution')
const cases = require('../cases.json')

describe('Testing Calendar Matching Algo', ()=>{
    test('Test if the function exists', ()=>{
        expect(typeof calendarMatching).toEqual('function')
    })

    const {JSONTests, TestResults} = cases
    JSONTests.forEach((item, index)=>{
        test(`Test ${index}`, ()=>{
            const {calendar1, calendar2, dailyBounds1, dailyBounds2, meetingDuration} = item
            expect(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)).toEqual(TestResults[index]['Expected'])
        })
    })
})