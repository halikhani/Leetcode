# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:


# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input: root = [1,2]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # got help from neetcode to solve this problem
        
        result = 0
        
        # defining a function to calculate height of the sub-trees
        def dfs(root):
            # interesting tip here: should use either nonlocal before the global var or defnine result as [0] (list)             # which is a mutable object
            nonlocal result
            if not root:
                return -1
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            
            # the max diameter would be the max of the preiously calculated answers or the height of left and right               # children plus 2 which is the sum of the edges from root to left and right immediate children
            result = max(result, 2 + left_height + right_height)
            
            # the following formula returns the height of each node in a recursive manner
            return 1 + max(left_height, right_height)
        dfs(root)
        
        return result