import unittest
from solution import calendarMatching

TestResults = [
        {
          "Expected": [
            [
              "11:30",
              "12:00"
            ],
            [
              "15:00",
              "16:00"
            ],
            [
              "18:00",
              "18:30"
            ]
          ]
        },
        {
          "Expected": [
            [
              "11:30",
              "12:00"
            ],
            [
              "15:00",
              "16:00"
            ],
            [
              "18:00",
              "18:30"
            ]
          ]
        },
        {
          "Expected": [
            [
              "15:00",
              "16:00"
            ]
          ]
        },
        {
          "Expected": [
            [
              "8:00",
              "9:00"
            ],
            [
              "15:00",
              "16:00"
            ]
          ]
        },
        {
          "Expected": [
            
          ]
        },
        {
          "Expected": [
            [
              "9:30",
              "10:00"
            ],
            [
              "11:15",
              "11:30"
            ],
            [
              "13:30",
              "14:15"
            ],
            [
              "18:00",
              "18:30"
            ]
          ]
        },
        {
          "Expected": [
            
          ]
        },
        {
          "Expected": [
            [
              "18:00",
              "20:00"
            ]
          ]
        },
        {
          "Expected": [
            [
              "9:30",
              "16:30"
            ]
          ]
        },
        {
          "Expected": [
            [
              "9:30",
              "16:30"
            ]
          ]
        },
        {
          "Expected": [
            [
              "9:30",
              "16:30"
            ]
          ]
        },
        {
          "Expected": [
            [
              "8:30",
              "9:00"
            ],
            [
              "10:30",
              "11:15"
            ],
            [
              "19:00",
              "20:00"
            ]
          ]
        }
      ]
JSONTests = [
        {
          "calendar1": [
            [
              "9:00",
              "10:30"
            ],
            [
              "12:00",
              "13:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:30"
            ],
            [
              "12:30",
              "14:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "9:00",
            "20:00"
          ],
          "dailyBounds2": [
            "10:00",
            "18:30"
          ],
          "meetingDuration": 30
        },
        {
          "calendar1": [
            [
              "9:00",
              "10:30"
            ],
            [
              "12:00",
              "13:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:30"
            ],
            [
              "12:30",
              "14:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "9:00",
            "20:00"
          ],
          "dailyBounds2": [
            "10:00",
            "18:30"
          ],
          "meetingDuration": 30
        },
        {
          "calendar1": [
            [
              "9:00",
              "10:30"
            ],
            [
              "12:00",
              "13:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:30"
            ],
            [
              "12:30",
              "14:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "9:00",
            "20:00"
          ],
          "dailyBounds2": [
            "10:00",
            "18:30"
          ],
          "meetingDuration": 45
        },
        {
          "calendar1": [
            [
              "9:00",
              "10:30"
            ],
            [
              "12:00",
              "13:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:30"
            ],
            [
              "12:30",
              "14:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "8:00",
            "20:00"
          ],
          "dailyBounds2": [
            "7:00",
            "18:30"
          ],
          "meetingDuration": 45
        },
        {
          "calendar1": [
            [
              "8:00",
              "10:30"
            ],
            [
              "11:30",
              "13:00"
            ],
            [
              "14:00",
              "16:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:30"
            ],
            [
              "12:30",
              "14:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "8:00",
            "18:00"
          ],
          "dailyBounds2": [
            "7:00",
            "18:30"
          ],
          "meetingDuration": 15
        },
        {
          "calendar1": [
            [
              "10:00",
              "10:30"
            ],
            [
              "10:45",
              "11:15"
            ],
            [
              "11:30",
              "13:00"
            ],
            [
              "14:15",
              "16:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:00"
            ],
            [
              "12:30",
              "13:30"
            ],
            [
              "14:30",
              "15:00"
            ],
            [
              "16:00",
              "17:00"
            ]
          ],
          "dailyBounds1": [
            "9:30",
            "20:00"
          ],
          "dailyBounds2": [
            "9:00",
            "18:30"
          ],
          "meetingDuration": 15
        },
        {
          "calendar1": [
            [
              "10:00",
              "10:30"
            ],
            [
              "10:45",
              "11:15"
            ],
            [
              "11:30",
              "13:00"
            ],
            [
              "14:15",
              "16:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:00"
            ],
            [
              "10:30",
              "20:30"
            ]
          ],
          "dailyBounds1": [
            "9:30",
            "20:00"
          ],
          "dailyBounds2": [
            "9:00",
            "22:30"
          ],
          "meetingDuration": 60
        },
        {
          "calendar1": [
            [
              "10:00",
              "10:30"
            ],
            [
              "10:45",
              "11:15"
            ],
            [
              "11:30",
              "13:00"
            ],
            [
              "14:15",
              "16:00"
            ],
            [
              "16:00",
              "18:00"
            ]
          ],
          "calendar2": [
            [
              "10:00",
              "11:00"
            ],
            [
              "10:30",
              "16:30"
            ]
          ],
          "dailyBounds1": [
            "9:30",
            "20:00"
          ],
          "dailyBounds2": [
            "9:00",
            "22:30"
          ],
          "meetingDuration": 60
        },
        {
          "calendar1": [
            
          ],
          "calendar2": [
            
          ],
          "dailyBounds1": [
            "9:30",
            "20:00"
          ],
          "dailyBounds2": [
            "9:00",
            "16:30"
          ],
          "meetingDuration": 60
        },
        {
          "calendar1": [
            
          ],
          "calendar2": [
            
          ],
          "dailyBounds1": [
            "9:00",
            "16:30"
          ],
          "dailyBounds2": [
            "9:30",
            "20:00"
          ],
          "meetingDuration": 60
        },
        {
          "calendar1": [
            
          ],
          "calendar2": [
            
          ],
          "dailyBounds1": [
            "9:30",
            "16:30"
          ],
          "dailyBounds2": [
            "9:30",
            "16:30"
          ],
          "meetingDuration": 60
        },
        {
          "calendar1": [
            [
              "7:00",
              "7:45"
            ],
            [
              "8:15",
              "8:30"
            ],
            [
              "9:00",
              "10:30"
            ],
            [
              "12:00",
              "14:00"
            ],
            [
              "14:00",
              "15:00"
            ],
            [
              "15:15",
              "15:30"
            ],
            [
              "16:30",
              "18:30"
            ],
            [
              "20:00",
              "21:00"
            ]
          ],
          "calendar2": [
            [
              "9:00",
              "10:00"
            ],
            [
              "11:15",
              "11:30"
            ],
            [
              "11:45",
              "17:00"
            ],
            [
              "17:30",
              "19:00"
            ],
            [
              "20:00",
              "22:15"
            ]
          ],
          "dailyBounds1": [
            "6:30",
            "22:00"
          ],
          "dailyBounds2": [
            "8:00",
            "22:30"
          ],
          "meetingDuration": 30
        }
      ]
    
class CalendarMatchingTests(unittest.TestCase):
    def test_calendar_matching(self):
        for i in range(0, len(JSONTests)):
            calendar1 = JSONTests[i]['calendar1']
            calendar2 = JSONTests[i]['calendar2']
            dailyBounds1 = JSONTests[i]['dailyBounds1']
            dailyBounds2 = JSONTests[i]['dailyBounds2']
            meetingDuration = JSONTests[i]['meetingDuration']
            result = calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration)
            self.assertEqual(result, TestResults[i]['Expected'])