# Given the root of a binary tree, 
# return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,3,2]


# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 
# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        elif root.left is None or root.right is None:
            if root.left is None and  root.right is None:
                return [root.val]
            elif root.left is None:
                return [root.val] + self.inorderTraversal(root.right)
            else:
                return self.inorderTraversal(root.left) + [root.val] 
        else:
            result = []
            result += self.inorderTraversal(root.left)
            result += [root.val]
            result += self.inorderTraversal(root.right) 
            return result