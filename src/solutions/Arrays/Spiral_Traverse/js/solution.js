/**
 * Write a function that takes in an n x m two-dimensional array (that can be
 *   square-shaped when n == m) and returns a one-dimensional array of all the
 *   array's elements in spiral order.
 *   Spiral order starts at the top left corner of the two-dimensional array, goes
 *   to the right, and proceeds in a spiral pattern all the way until every element
 *   has been visited.
 *   Sample Input
 *   array = [
 *   [1,   2,  3, 4],
 *   [12, 13, 14, 5],
 *   [11, 16, 15, 6],
 *   [10,  9,  8, 7],
 * ]
 * 
 * Sample Output
 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
 * Time: O(n) time | O(n) space - where n is the total number of elements in the array
 */

function spiralTraverse(array){
  let startRow = 0
  let endRow = array.length - 1
  let startCol = 0
  let endCol = array[0].length - 1
  let res = []

  while(startRow <= endRow && startCol <= endCol){
    //top-right
    for(let col = startCol; col <= endCol; col++ ){
      res.push(array[startRow][col])
    }
    //right-bottom
    for(let row = startRow+1; row <= endRow; row++){
      res.push(array[row][endCol])
    }
    //bottom-right - left
    for(let col = endCol-1; col >= startCol; col--){
      if(startRow === endRow) break;
      res.push(array[endRow][col])
    }
    //bottom-right - top
    for(let row = endRow - 1; row > startRow; row--){
      if(startCol === endCol) break;
      res.push(array[row][startCol])
    }

    startRow++
    endRow--
    startCol++
    endCol--

  }
  console.log(res)
  return res
}

module.exports = spiralTraverse