# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
 

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

class Solution:
    def rob(self, nums: List[int]) -> int:
        # if we choose first e in nums, we have to solve it for the nums[2:] and add it to nums[0]
        # if we dont choose first e in nums, we should sole it for nums[1:]
        nums = nums[::-1]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            elif i == len(nums)-2:
                # we have to choose between selecting current idx and skip next, or vice versa
                nums[i] = max(nums[i], nums[i+1])
            else:
                # Either we choose current cell and add it to the pre-calculated value for nums[i+2], or we skip current cell and rob the adjacent house (i+1) and make the profit that was calculated before for that idx
                nums[i] = max(nums[i+1], nums[i] + nums[i+2])
        return nums[0]