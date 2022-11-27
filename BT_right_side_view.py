# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

# Example 1:


# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:

# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = []
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            l_height = self.getHeight(root.left)
            r_height = self.getHeight(root.right)
            if l_height > r_height:
                return l_height + 1
            else:
                return r_height + 1
            
    
    def getCurrentLevelNodes(self, root: Optional[TreeNode], level) -> List[int]:
        if not root:
            return
        if level == 1:
            self.s.append(root.val)
        else:
            self.getCurrentLevelNodes(root.left, level-1)
            self.getCurrentLevelNodes(root.right, level-1)
            
        return self.s
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = self.getHeight(root)
        result = []
        for h in range(1, height + 1):
            # the right-most item of each level should be stored in the result list
            cur_lev_nodes = self.getCurrentLevelNodes(root, h)
            self.s = []
            if cur_lev_nodes:
                result.append(cur_lev_nodes[-1]) 
        return result
    
        # neetcode solution
#         result = []
#         q = collections.deque([root])
        
#         while q:
#             rightmost = None
#             qlen = len(q)
            
#             for i in range(qlen):
#                 # popping the leftmost node and add its children to the q
#                 l_node = q.popleft()
                
#                 if l_node:
#                     rightmost = l_node
#                     q.append(rightmost.left)
#                     q.append(rightmost.right)
#                     # keeping potential rightmost node of each level and add it to the res if not None
                
#             if rightmost:
#                 result.append(rightmost.val)
                    
#         return result