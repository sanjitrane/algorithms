/**
 * Write a function that takes in an n x m two-dimensional array (that can be
 *   square-shaped when n == m) and returns a one-dimensional array of all the
 *   array's elements in zigzag order.
 * 
 *   Zigzag order starts at the top left corner of the two-dimensional array, goes
 *   down by one element, and proceeds in a zigzag pattern all the way to the
 *   bottom right corner.
 * 
 * Sample Input
 * array = [
 *   [1,  3,  4, 10],
 *   [2,  5,  9, 11],
 *   [6,  8, 12, 15],
 *   [7, 13, 14, 16],
 * ]
 * 
 * Sample Output
 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
 * 
 * Time: O(n) | Space: O(n)  - where n is the total number of elements in the two-dimensional array
 */

function zigzagTraverse(array){
    const results = []
    const height = array.length - 1
    const width = array[0].length - 1
    let row = 0
    let col = 0
    let isGoingDown = true
    while( !isOutOfBounds(row, col, width, height)){
        results.push(array[row][col])
        if(isGoingDown){
            if(col === 0 || row === height){
                isGoingDown = false
                if(row === height){
                    col++
                }else{
                    row++
                }
            }else{
                row++
                col--
            }
        }else{
            if(col === width || row === 0){
                isGoingDown = true
                if(col === width){
                    row++
                }else{
                    col++
                }
            }else{
                row--
                col++
            }
        }
    }
    return results
}

function isOutOfBounds(row, col, width, height){
    return row < 0 || row > height || col < 0 || col > width
}

module.exports = zigzagTraverse