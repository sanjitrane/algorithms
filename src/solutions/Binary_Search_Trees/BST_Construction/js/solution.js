/**
 * Write a BST class for a Binary Search Tree. The class should
 *   support:
 * 
 *   Inserting values with the insert method.
 *   Removing values with the remove method; this method should
 *   only remove the first instance of a given value.
 *   Searching for values with the contains method.
 * 
 *   Note that you can't remove values from a single-node tree. In other words,
 *   calling the remove method on a single-node tree should simply not
 *   do anything.
 * 
 *   Each BST node has an integer value, a
 *   left child node, and a right child node. A node is
 *   said to be a valid BST node if and only if it satisfies the BST
 *   property: its value is strictly greater than the values of every
 *   node to its left; its value is less than or equal to the values
 *   of every node to its right; and its children nodes are either valid
 *   BST nodes themselves or None / null.
 * 
 * Sample Usage
 * Assume the following BST has already been created:
 *          10
 *        /     \
 *       5      15
 *     /   \   /   \
 *    2     5 13   22
 *  /           \
 * 1            14
 * 
 * All operations below are performed sequentially.
 * 
 * insert(12):   10
 *             /     \
 *            5      15
 *          /   \   /   \
 *         2     5 13   22
 *       /        /  \
 *      1        12  14
 * 
 * 
 * remove(10):   12
 *             /     \
 *            5      15
 *          /   \   /   \
 *         2     5 13   22
 *       /           \
 *      1            14
 * 
 * 
 * contains(15): true
 * 
 * Average (all 3 methods): Time: O(log(n)) | Space: O(1) - where n is the number of nodes in the BST
 * Worst (all 3 methods): Time: O(n) time | Space: O(1) - where n is the number of nodes in the BST
 */

class BST{
  constructor(value){
    this.value = value
    this.left = null
    this.right = null
  }

  //Average : Time - O(log(n)) | Space - O(log(n)) - space due to stack execution from recursive calls
  //Worst: Time - O(n) | Space O(n)
  insert(value){
    if(value < this.value){
      if(this.left === null){
        this.left = new BST(value)
      }else{
        this.left.insert(value)
      }
    }else{
      if(this.right === null){
        this.right = new BST(value)
      }else{
        this.right.insert(value)
      }
    }
    return this
  }

  //Average : Time O(log(n)) | Space O(log(n)) 
  //Worst : Time O(n) | Space O(n)
  contains(value){
    if(value < this.value){
      if(this.left === null){
        return false
      }else{
        this.left.contains(value)
      }
    }else{
      if(this.right === null){
        return false
      }else{
        this.right.contains(value)
      }
    }
    return true
  }

  remove(value){
    return this
  }
}

module.exports = BST