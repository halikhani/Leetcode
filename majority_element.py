# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Using Boyer-Moore approach
        count = 0
        current_maj = 0
        
        for n in nums:
            if n == current_maj:
                count += 1
            else:
                if count == 0:
                    count = 1
                    current_maj = n
                else:
                    count -= 1
        return current_maj
        