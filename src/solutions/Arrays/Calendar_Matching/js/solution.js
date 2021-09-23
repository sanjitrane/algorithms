/**
 * Imagine that you want to schedule a meeting of a certain duration with a
 *   co-worker. You have access to your calendar and your co-worker's calendar
 *   (both of which contain your respective meetings for the day, in the form of
 *   [startTime, endTime]), as well as both of your daily bounds
 *   (i.e., the earliest and latest times at which you're available for meetings
 *   every day, in the form of [earliestTime, latestTime]).
 * 
 *   Write a function that takes in your calendar, your daily bounds, your
 *   co-worker's calendar, your co-worker's daily bounds, and the duration of the
 *   meeting that you want to schedule, and that returns a list of all the time
 *   blocks (in the form of [startTime, endTime]) during which you
 *   could schedule the meeting, ordered from earliest time block to latest.
 * 
 *   Note that times will be given and should be returned in military time. For
 *   example: 8:30, 9:01, and 23:56.
 * 
 *   Also note that the given calendar times will be sorted by start time in
 *   ascending order, as you would expect them to appear in a calendar application
 *   like Google Calendar.
 *  Sample Input
 *  calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
 *  dailyBounds1 = ['9:00', '20:00']
 *  calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
 *  dailyBounds2 = ['10:00', '18:30']
 *  meetingDuration = 30
 * 
 *  Sample Output
 * [['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
 * Time: O(c1 + c2) | Space: O(c1 + c2) - where c1 and c2 are the respective numbers of meetings in calendar1 and calendar2
 */

function calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration){
    const updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    const updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    const mergedCalendar = mergeCalendar(updatedCalendar1, updatedCalendar2)
    const flattenedCalendar = flattenCalendar(mergedCalendar)
    return getAvailableSlots(flattenedCalendar, meetingDuration)
}

//Adds a new meeting at the start of the calendar and one at the end
function updateCalendar(calendar, dailyBounds){
    const updated = [['0:00', dailyBounds[0]],...calendar,[dailyBounds[1], '23:59']]
    return updated.map(meeting=> meeting.map(timeToMinutes))
}

//Converts the time string to minutes
function timeToMinutes(time){
    const [hours, minutes] = time.split(':').map(str=>parseInt(str))
    return hours * 60 + minutes
}
// Merge the calendars in ascending start time
function mergeCalendar(calendar1, calendar2){
    const merged = []
    let i = 0;
    let j = 0;
    while(i < calendar1.length && j < calendar2.length){
        const meeting1 = calendar1[i]
        const meeting2 = calendar2[j]
        if(meeting1[0] < meeting2[0]){
            merged.push(meeting1)
            i++
        }else{
            merged.push(meeting2)
            j++
        }
    }
    while(i < calendar1.length) merged.push(calendar1[i++])
    while(j < calendar2.length) merged.push(calendar2[j++])
    return merged
}

//Flattens the calendar by merging overlapping meetings
function flattenCalendar(calendar){
    const flattened = [calendar[0].slice()]
    for(let i = 1; i < calendar.length; i++){
        const currMeeting = calendar[i]
        const prevMeeting = flattened[flattened.length - 1]
        const [currStart, currEnd] = currMeeting
        const [prevStart, prevEnd] = prevMeeting
        if( prevEnd > currStart){
            const newPrevMeeting = [prevStart, Math.max(currEnd, prevEnd)]
            flattened[flattened.length - 1] = newPrevMeeting
        }else{
            flattened.push(currMeeting.slice())
        }
    }
    return flattened
}

// check for start and end time and find available slots fitting the meeting duration
function getAvailableSlots(calendar, meetingDuration){
    const matchingSlots = []
    for(let i = 1; i < calendar.length; i++){
        const start = calendar[i - 1][1]
        const end = calendar[i][0]
        const availableDuration = end - start
        if(availableDuration >= meetingDuration){
            matchingSlots.push([start, end])
        }
    }
    return matchingSlots.map(meeting=> meeting.map(minutesToTime))
}

//converts minutes to the time format
function minutesToTime(minutes){
    const hours = Math.floor(minutes / 60)
    const mins = minutes % 60
    const minStr = mins < 10 ? '0' + mins.toString() : mins.toString()
    const hourStr = hours.toString()
    return hourStr + ':' + minStr
}

module.exports = calendarMatching