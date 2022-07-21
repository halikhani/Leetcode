# Longest Continuous Increasing Subsequence

# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
# 4.


# Example 2:

# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
# increasing.
 

# Constraints:

# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_seq_len = 0
        current_seq = 0
        for i in range(len(nums)):
            if i == 0:
                current_seq = 1
                if current_seq >= longest_seq_len:
                    longest_seq_len = current_seq
                continue
            else:
                if nums[i-1] < nums[i]:
                    if current_seq != 0:
                        current_seq += 1
                    if current_seq == 0:
                        current_seq = 2
                else:
                    current_seq = 1
                if current_seq >= longest_seq_len:
                    longest_seq_len = current_seq
            
        return longest_seq_len