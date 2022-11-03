# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]
 

# Constraints:

# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # got help from neetcode for this problem
        
        res = []
        
        subset = []
        
        def dfs(i):
            print(subset)
            if i >= len(nums):
                res.append(subset.copy())
                # the reason we use copy() is that subset is going to be modified in the future so it would affect                   all the previous values of the subset list
                return
            
            # branch of the dfs that includes nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # branch of the dfs that doesn't include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res