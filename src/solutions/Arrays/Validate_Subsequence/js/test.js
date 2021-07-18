const isValidSubsequence =  require('./solution')

const jsonTests=[
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      -1,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      22,
      25,
      6
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      25
    ]
  },
  {
    "array": [
      1,
      1,
      1,
      1,
      1
    ],
    "sequence": [
      1,
      1,
      1
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10,
      12
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      4,
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      23,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      22,
      25,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      22,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      -1,
      -1
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      -1,
      -1,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      -1,
      -2
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      26
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      25,
      22,
      6,
      -1,
      8,
      10
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      26,
      22,
      8
    ]
  },
  {
    "array": [
      1,
      1,
      6,
      1
    ],
    "sequence": [
      1,
      1,
      1,
      6
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      1,
      6,
      -1,
      10,
      11,
      11,
      11,
      11
    ]
  },
  {
    "array": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10
    ],
    "sequence": [
      5,
      1,
      22,
      25,
      6,
      -1,
      8,
      10,
      10
    ]
  }
]

const expectedOutput=[true, true, true, true, true, true, true, true, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false]

describe('Testing the isValidateSubsequence function',()=>{
  test('isValidSubsequence is a valid function', ()=>{
    expect(typeof isValidSubsequence).toEqual('function')
  })

  jsonTests.forEach((item,index)=>{
    test(`Test ${index}`,()=>{
      const {array, sequence} = jsonTests[index]
      expect(isValidSubsequence(array, sequence)).toEqual(expectedOutput[index]) 
    })
  })

})
