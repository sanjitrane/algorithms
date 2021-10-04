/**
 * Given an array of distinct positive integers representing coin denominations and a
 *   single non-negative integer n representing a target amount of
 *   money, write a function that returns the number of ways to make change for
 *   that target amount using the given coin denominations.
 * 
 *  Note that an unlimited amount of coins is at your disposal.
 *  Sample Input
 * n = 6
 * denoms = [1, 5]
 * 
 *  Sample Output
 *  2 // 1x1 + 1x5 and 6x1
 * 
 * Time: O(nd) | Space: O(n) - where n is the target amount and d is the number of coin denominations
 */

function numberOfWaysToMakeChange(n, denoms){
    const ways = new Array(n + 1).fill(0)
    ways[0] = 1
    for(const denom of denoms){
        for(let amount = 1; amount < n + 1; amount++){
            if(denom <= amount){
                ways[amount]+=ways[amount - denom]
            }
        }
    }
    return ways[n] 
}

module.exports= numberOfWaysToMakeChange