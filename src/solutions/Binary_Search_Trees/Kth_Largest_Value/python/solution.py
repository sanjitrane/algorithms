# Write a function that takes in a Binary Search Tree (BST) and a positive
#   integer k and returns the kth largest integer contained in the
#   BST.
# 
#   You can assume that there will only be integer values in the BST and that
#   k is less than or equal to the number of nodes in the tree.
# 
#   Also, for the purpose of this question, duplicate integers will be treated as
#   distinct values. In other words, the second largest value in a BST containing
#   values {5, 7, 7} will be 7 —not 5.
# 
#   Each BST node has an integer value, a
#   left child node, and a right child node. A node is
#   said to be a valid BST node if and only if it satisfies the BST
#   property: its value is strictly greater than the values of every
#   node to its left; its value is less than or equal to the values
#   of every node to its right; and its children nodes are either valid
#   BST nodes themselves or None / null.
#   Sample Input
#   tree =  15
#        /     \\
#       5      20
#     /   \\   /   \\
#    2     5 17   22
#  /   \\         
# 1     3       
# 
# k = 3
# 
# Sample Output
# 17
# 
# Time: O(h + k) | Space: O(h) - where h is the height of the tree and k is the input parameter

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#Solution 1
#Time: O(n) | Space O(n)
def findKthLargestValueInBST(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, k, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, k, sortedNodeValues):
    if node== None:
        return
    inOrderTraverse(node.left, k, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, k, sortedNodeValues)

#Solution 2
#Time: O(h+k) | Space: O(h)

class TreeInfo:
    def __init__(self, numberOfNodesVisited, lastVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.lastVisitedNodeValue = lastVisitedNodeValue

def findKthLargestValueInBST1(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.lastVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.lastVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)



 