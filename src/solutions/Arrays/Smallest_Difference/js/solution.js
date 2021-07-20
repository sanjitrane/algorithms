/**
 * Write a function that takes in two non-empty arrays of integers, finds the
 *   pair of numbers (one from each array) whose absolute difference is closest to
 *   zero, and returns an array containing these two numbers, with the number from
 *   the first array in the first position.
 *   Note that the absolute difference of two integers is the distance between
 *   them on the real number line. For example, the absolute difference of -5 and 5
 *   is 10, and the absolute difference of -5 and -4 is 1.
 *   You can assume that there will only be one pair of numbers with the smallest
 *   difference.
 * Sample Input
 * 
 * arrayOne = [-1, 5, 10, 20, 28, 3]
 * arrayTwo = [26, 134, 135, 15, 17]
 * Sample Output
 * [28, 26]
 * Time O(nlog(n) + mlog(m)) | Space O(1) - where n is the length of the first input array and m is the length of the second input array
 */

 //arrayOne = [-1, 3, 5, 10, 20, 28]
 //arrayTwo = [15, 17, 26, 134, 135]

function smallestDifference(arrayOne, arrayTwo){
  arrayOne.sort((a,b)=> a-b)
  arrayTwo.sort((a,b)=> a-b)
  let p1 = 0
  let p2 = 0
  let currentSum = Infinity
  let smallest = Infinity
  let pair = []
  while(p1 < arrayOne.length && p2 < arrayTwo.length){
    let fNum = arrayOne[p1]
    let sNum = arrayTwo[p2]
    if(fNum > sNum){
      currentSum = fNum - sNum
      p2++
    }else if(sNum > fNum){
      currentSum = sNum - fNum
      p1++
    }else{
      return [fNum, sNum]
    }
    if(smallest > currentSum){
      smallest = currentSum
      pair = [fNum, sNum]
    }
  }
  return pair
}

module.exports = smallestDifference