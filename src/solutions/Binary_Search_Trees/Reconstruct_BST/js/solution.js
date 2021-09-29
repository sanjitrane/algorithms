/**
 * The pre-order traversal of a Binary Tree is a traversal technique that starts
 *   at the tree's root node and visits nodes in the following order:
 *   Current node
 *   Left subtree
 *   Right subtree
 * 
 *   Given a non-empty array of integers representing the pre-order traversal of a
 *   Binary Search Tree (BST), write a function that creates the relevant BST and
 *   returns its root node.
 * 
 *   The input array will contain the values of BST nodes in the order in which
 *   these nodes would be visited with a pre-order traversal.
 * 
 *   Each BST node has an integer value, a
 *   left child node, and a right child node. A node is
 *   said to be a valid BST node if and only if it satisfies the BST
 *   property: its value is strictly greater than the values of every
 *   node to its left; its value is less than or equal to the values
 *   of every node to its right; and its children nodes are either valid
 *   BST nodes themselves or None / null.
 *  
 * Sample Input
 * 
 * preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
 * Sample Output
 * 
 *         10 
 *       /    \
 *      4      17
 *    /   \      \
 *   2     5     19
 *  /           /
 * 1           18 
 * 
 * Time: "O(n) | Space: O(n) - where n is the length of the input array"
 */

class BST{
    constructor(value, left, right){
        this.value = value
        this.left = left
        this.right = right
    }
}

//Solution 1
//Time: O(n^2) | Space O(n)
function recontructBst(preOrderTraversalValues){
    if(preOrderTraversalValues.length === 0) return null
    const currentValue = preOrderTraversalValues[0]
    let rightSubTreeRootIdx = preOrderTraversalValues.length
    for(let i = 1; i < preOrderTraversalValues.length; i++){
        const value = preOrderTraversalValues[i]
        if(value >= currentValue){
            rightSubTreeRootIdx = i
            break;
        }
    }

    const leftSubTree = recontructBst(preOrderTraversalValues.slice(1, rightSubTreeRootIdx))
    const rightSubTree = recontructBst(preOrderTraversalValues.slice(rightSubTreeRootIdx))
    return new BST(currentValue, leftSubTree, rightSubTree)
}

//Solution 2
// Time: O(n) | Space: O(n)

class TreeInfo{
    constructor(rightIdx){
        this.rightIdx = rightIdx
    }
}

function reconstructBst1(preOrderTraversalValues){
    const treeInfo = new TreeInfo(0)
    return reconstructBstFromRange(-Infinity, Infinity, preOrderTraversalValues, treeInfo)
}

function reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubTreeInfo){
    if(currentSubTreeInfo.rightIdx === preOrderTraversalValues.length) return null
    const rootValue = preOrderTraversalValues[currentSubTreeInfo.rightIdx]

    if(rootValue < lowerBound || rootValue > upperBound) return null
    currentSubTreeInfo.rightIdx++
    const leftSubTree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubTreeInfo)
    const rightSubTree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubTreeInfo)
    return new BST(rootValue, leftSubTree, rightSubTree)
}