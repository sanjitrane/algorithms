/**
 * Write a function that takes in an array of integers and returns a boolean
 *   representing whether the array is monotonic.
 *   An array is said to be monotonic if its elements, from left to right, are
 *   entirely non-increasing or entirely non-decreasing.
 *   Non-increasing elements aren't necessarily exclusively decreasing; they simply
 *   don't increase. Similarly, non-decreasing elements aren't necessarily
 *   exclusively increasing; they simply don't decrease.
 * Note that empty arrays and arrays of one element are monotonic.
 * Sample Input
 * array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
 * Sample Output
 * true
 * Time: O(n) time | Space: O(1) - where n is the length of the array
 */

function monotonicArray(array){
  if(array.length <=2) return true
  let dir = array[1] - array[0]
  for(let i = 2; i< array.length;i++){
    if(dir === 0){
      dir = array[i] - array[i-1]
      continue
    }
    if(breaksDir(dir, array[i-1], array[i])){
      return false
    }
  }
  return true
}

function breaksDir(dir, prevInt, currInt){
  const diff = currInt - prevInt
  if(dir > 0){
    return diff < 0
  }
  return diff > 0
}

function isMonotonic(array){
  let isNonIncreasing = true
  let isNonDecreasing = true
  for(let i = 1; i < array.length; i++){
      if(array[i] < array[i-1]) isNonDecreasing = false
      if(array[i] > array[i - 1]) isNonIncreasing = false
  }
  return isNonIncreasing || isNonDecreasing
}

module.exports = {monotonicArray, isMonotonic}