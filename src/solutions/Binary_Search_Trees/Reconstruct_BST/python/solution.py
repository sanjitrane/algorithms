# The pre-order traversal of a Binary Tree is a traversal technique that starts
#   at the tree's root node and visits nodes in the following order:
#   Current node
#   Left subtree
#   Right subtree
# 
#   Given a non-empty array of integers representing the pre-order traversal of a
#   Binary Search Tree (BST), write a function that creates the relevant BST and
#   returns its root node.
# 
#   The input array will contain the values of BST nodes in the order in which
#   these nodes would be visited with a pre-order traversal.
# 
#   Each BST node has an integer value, a
#   left child node, and a right child node. A node is
#   said to be a valid BST node if and only if it satisfies the BST
#   property: its value is strictly greater than the values of every
#   node to its left; its value is less than or equal to the values
#   of every node to its right; and its children nodes are either valid
#   BST nodes themselves or None / null.
#  
# Sample Input
# 
# preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
# Sample Output
# 
#         10 
#       /    \
#      4      17
#    /   \      \
#   2     5     19
#  /           /
# 1           18 
# 
# Time: "O(n) | Space: O(n) - where n is the length of the input array"#

class BST:
    def __init__(self, value, left=None, right=None):
        self.value =  value
        self.left = left
        self.right = right

# Sol 1 
# Time O(n^2) | Space O(h)
def reconstruct(preOrderTraversalValues):
    if len(preOrderTraversalValues)== 0:
        return None
    
    currentValue = preOrderTraversalValues[0]
    rightSubTreeRootIdx = len(preOrderTraversalValues)
    for i, value in enumerate(preOrderTraversalValues):
        value = preOrderTraversalValues[i]
        if value >= currentValue:
            rightSubTreeRootIdx = i
            break
    
    leftSubTree = reconstruct(preOrderTraversalValues[1:rightSubTreeRootIdx])
    rightSubTree = reconstruct(preOrderTraversalValues[rightSubTreeRootIdx:])
    return BST(currentValue, leftSubTree, rightSubTree)


#Sol 2

class TreeInfo:
    def __init(self, rootIdx):
        self.rootIdx = rootIdx

def recontruct1(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBSTFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

def reconstructBSTFromRange(lowerBound, upperBound, preOrderTraversalValues, currentTreeInfo):
    if currentTreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    
    rootValue = preOrderTraversalValues[currentTreeInfo.rootIdx]

    if rootValue <= lowerBound or rootValue >= upperBound:
        return None

    currentTreeInfo.rootIdx+=1
    leftSubTree = reconstructBSTFromRange(lowerBound, rootValue, preOrderTraversalValues, currentTreeInfo)
    rightSubTree = reconstructBSTFromRange(rootValue, upperBound, preOrderTraversalValues, currentTreeInfo)
    return BST(rootValue, leftSubTree, rightSubTree)


    