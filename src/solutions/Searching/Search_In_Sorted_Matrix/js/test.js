const searchInSortedMatrix = require('./solution')
const cases = require('../cases.json')

describe('Testig Search In Sorted Matrix Algo', ()=>{
  test('searchInSortedMatrix function exists', ()=>{
    expect(typeof searchInSortedMatrix).toEqual('function')
  })

  const {JSONTests, TestResults} = cases
  JSONTests.forEach((item, index)=>{
    const {matrix, target} = item
    test(`Test ${index}`, ()=>{
      expect(searchInSortedMatrix(matrix, target)).toEqual(TestResults[index]['Expected'])
    })
  })
})