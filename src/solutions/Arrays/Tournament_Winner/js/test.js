const tournamentWinner = require('./solution')
const cases = require('../cases.json')

describe('Testing the Tournament Winner function',()=>{
  test('Test if the function exists', ()=>{
    expect(typeof tournamentWinner).toEqual('function')
  })

  const {JSONTests, expectedOutput} = cases
  JSONTests.forEach((item, index)=>{
    const {competitions, results} = item
    test(`Test ${index}`,()=>{
      expect(tournamentWinner(competitions, results)).toEqual(expectedOutput[index])
    })
  })
})