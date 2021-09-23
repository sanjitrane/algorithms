/**
 * Write a function that takes in an array of at least two integers and that
 *   returns an array of the starting and ending indices of the smallest subarray
 *   in the input array that needs to be sorted in place in order for the entire
 *   input array to be sorted (in ascending order).
 * 
 *   If the input array is already sorted, the function should return
 *   [-1, -1]
 * 
 * Sample Input
 * array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
 * Sample Output
 * [3, 9]
 * 
 * Time: O(n) | Space: O(1) - where n is the length of the input array
 */

function subarraySort(array){
    let minOutOfOrder = Infinity
    let maxOutOfOrder = -Infinity
    for(let i = 0; i < array.length; i++){
        const num = array[i]
        if(isNotSorted(i, num, array)){
            minOutOfOrder = Math.min(num, minOutOfOrder)
            maxOutOfOrder = Math.max(num, maxOutOfOrder)
        }
    }
    if(minOutOfOrder === Infinity) return [-1,-1]
    let minSubOrderIdx = 0
    while(minOutOfOrder >= array[minSubOrderIdx]){
        minSubOrderIdx++
    }
    let maxSubOrderIdx = array.length - 1
    while(maxOutOfOrder <= array[maxSubOrderIdx]){
        maxSubOrderIdx--
    }
    return [minSubOrderIdx, maxSubOrderIdx]
}

function isNotSorted(i, num, array){
    if(i === 0) return num > array[i + 1]
    if(i === array.length - 1) return num < array[i - 1]
    return num < array[i - 1] || num > array[i + 1] 
}

module.exports = subarraySort