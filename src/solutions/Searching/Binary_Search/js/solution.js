/**
 * Write a function that takes in a sorted array of integers as well as a target
 *   integer. The function should use the Binary Search algorithm to determine if
 *   the target integer is contained in the array and should return its index if it
 *   is, otherwise -1.
 * 
 *   If you're unfamiliar with Binary Search, we recommend watching the Conceptual
 *   Overview section of this question's video explanation before starting to code.
 * 
 * Sample Input
 * array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
 * target = 33
 * 
 * Sample Output
 * 3
 * 
 * Time: O(log(n)) | Space: O(1)  - where n is the length of the input array
 */

function binarySearch(array, target){
  if(!array.length) return -1
  let start = 0
  let end = array.length - 1
  let mid 
  while(start <= end){
    mid = Math.floor((end+start)/2)
    if(array[mid] > target){
      end = mid - 1
    }else if(array[mid] < target){
      start = mid + 1
    }else{
      return mid
    }
  }
  return -1
}

module.exports = binarySearch