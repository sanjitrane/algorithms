/** 
 * Write a function that takes in a non-empty array of distinct integers and an
 * integer representing a target sum. If any two numbers in the input array sum
 * up to the target sum, the function should return them in an array, in any
 * order. If no two numbers sum up to the target sum, the function should return
 * an empty array.
 * Note that the target sum has to be obtained by summing two different integers
 * in the array; you can't add a single integer to itself in order to obtain the
 * target sum.
 * You can assume that there will be at most one pair of numbers summing up to
 * the target sum.
 * "spaceTime": 
 *          "O(n) time | O(n) space - where n is the length of the input array",
 *          "O(nlog(n)) time | O(1) space"
 * 
 * Sample Input = [3, 5, -4, 8, 11, 1, -1, 6]
 * targetSum = 10
 * 
 * Sample Output
 * [-1, 11] // the numbers could be in reverse order
 * 
 * To Test: jest Two_Number_Sum --watch
*/

// Time: O(nlog(n)) | Space: O(1)
function twoNumberSum(array, sum){
  if(!array.length) return []
  array.sort((a,b)=> a - b)
  let left = 0
  let right = array.length - 1
  while(left < right){
    const total = array[left] + array[right]
    if(total === sum){
      return [array[left], array[right]]
    }else if(total < sum){
      left++
    }else{
      right--
    }
  }
  return []
}

// Time: O(n) | Space: O(n)
function twoNumberSum2(array, sum){
  if(!array.length) return []
  const nums = {}
  for(const num of array){
    const potentialMatch = sum - num
    if(potentialMatch in nums){
      return [potentialMatch, num]
    }else{
      nums[num] = true
    }
  }
  return []
}

module.exports= {twoNumberSum,twoNumberSum2}