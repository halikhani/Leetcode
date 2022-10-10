# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        
        for i, n in enumerate(nums):
            # skipping elements that are same as previous ones in the list
            if i > 0 and n == nums[i-1]:
                continue
            else:
                l, r = i+1, len(nums)-1
                while l < r:
                    threesum = n + nums[l] + nums[r]
                    if threesum < 0:
                        l += 1
                    elif threesum > 0:
                        r -= 1
                    else:
                        result.append([n, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
        return result
            
        
        
        
        
        