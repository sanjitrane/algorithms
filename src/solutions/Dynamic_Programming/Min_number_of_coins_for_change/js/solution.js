/**
 * Given an array of positive integers representing coin denominations and a
 *   single non-negative integer n representing a target amount of
 *   money, write a function that returns the smallest number of coins needed to
 *   make change for (to sum up to) that target amount using the given coin
 *   denominations.
 * 
 *   Note that you have access to an unlimited amount of coins. In other words, if
 *   the denominations are [1, 5, 10], you have access to an unlimited
 *   amount of 1s, 5s, and 10s.
 * 
 *   If it's impossible to make change for the target amount, return
 *   -1.
 *  Sample Input
 *  n = 7
 *  denoms = [1, 5, 10]
 * 
 *  Sample Output
 *  3 // 2x1 + 1x5
 * 
 * Time: O(nd) | Space: O(n) - where n is the target amount and d is the number of coin denominations
 */

function minNumberOfCoinsForChange(n, denoms){
    const numOfCoins = new Array(n + 1).fill(Infinity)
    numOfCoins[0] = 0
    for(const denom of denoms){
        for(let amount = 1; amount < numOfCoins.length; amount++){
            if(denom <= amount){
                numOfCoins[amount] = Math.min(numOfCoins[amount], numOfCoins[amount - denom]+1)
            }
        }
    }
    return numOfCoins[n] !== Infinity ? numOfCoins[n] : -1
}

module.exports = minNumberOfCoinsForChange