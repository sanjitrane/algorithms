/**
 * Write a function that takes in a non-empty array of integers that are sorted
 * in ascending order and returns a new array of the same length with the squares
 * of the original integers also sorted in ascending order.
 * Sample Input
 * array = [1, 2, 3, 5, 6, 8, 9]
 * Sample Output
 * [1, 4, 9, 25, 36, 64, 81]
 * Time: O(n) | Space: O(n) - where n is the length of the input 
 */

function sortedSquareArray(array){
  let start = 0
  let end = array.length - 1
  const res = new Array(array.length).fill(0)
  while(start <= end){
    const pos = end - start
    const val1 = array[start] * array[start]
    const val2 = array[end] * array[end]
    if(val1 > val2){
      res[pos] = val1
      start++
    }else{
      res[pos] = val2
      end--
    }
  }
  return res
}

module.exports = sortedSquareArray