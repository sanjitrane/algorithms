/**
 * Write a function that takes in a non-empty array of distinct integers and an
 *   integer representing a target sum. The function should find all quadruplets in
 *   the array that sum up to the target sum and return a two-dimensional array of
 *   all these quadruplets in no particular order.
 *   If no four numbers sum up to the target sum, the function should return an
 *   empty array.
 *  Sample Input
 *  array = [7, 6, 4, -1, 1, 2]
 *  targetSum = 16
 *
 *  Sample Output
 * [[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
 *
 * Time: Average: O(n^2) | O(n^2) - where n is the length of the input array
 * Worst: O(n^3) time | O(n^2) space - where n is the length of the input array
 */

function fourNumberSum(array, targetSum){
    const allPairs = {}
    const quads = []
    for(let i = 1; i < array.length - 1; i++){
        for(let j = i+1; j < array.length; j++){
            const currentSum = array[i] + array[j]
            const diff = targetSum - currentSum
            if(diff in allPairs){
                for(const pair of allPairs[diff]){
                    quads.push(pair.concat([array[i], array[j]]))
                }
            }
        }
        for(let k = 0; k < i; k++){
            const currentSum = array[k] + array[i]
            if(!(currentSum in allPairs)){
                allPairs[currentSum] = [[array[k], array[i]]]
            }else{
                allPairs[currentSum].push([array[k], array[i]])
            }
        }
    }
    return quads
}

module.exports=fourNumberSum