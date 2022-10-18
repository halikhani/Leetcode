# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # finding zero val indices
        is_zero = [True if n == 0 else False for n in nums]
        zero_num = sum(is_zero)
        
        non_zero_mult = 1
        for n in nums:
            if n == 0:
                continue
            else:
                non_zero_mult *= n
         
        result = []
        if zero_num >= 2:
            return [0 for i in range(len(nums))]
        elif zero_num == 1:
            for i in range(len(nums)):
                if is_zero[i]:
                    result.append(non_zero_mult)
                else:
                    result.append(0)
        else:
            for i in range(len(nums)):
                result.append(non_zero_mult/nums[i])
        
        return result