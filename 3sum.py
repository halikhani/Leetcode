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
    
    def twoSum(self, nums, target):
        result = []
        hashmap = {}
        for idx, val in enumerate(nums):
            res = target - val
            if res in hashmap.values():
                idx1 = hashmap.keys()[hashmap.values().index(res)]
                idx2 = idx
                result.append(idx1)
                result.append(idx2)
                return result
            else:
                hashmap[idx] = val
        result_vals = [nums[i] for i in result]
        # return result
        return result_vals
                
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result
        
        for idx, num in enumerate(nums):
            target = (-1)*num
            rem_list = nums[idx+1:]
            found_pairs = self.twoSum(rem_list, target)
            print(found_pairs)
            if len(found_pairs) > 0:
                r = found_pairs.insert(0, num)
                result.append(r)
        
        return result
        
        
        
        
        