class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        remaining_nums = set([i+1 for i in range(len(nums))])
        for e in nums:
            if e in remaining_nums:
                remaining_nums.remove(e)
        return list(remaining_nums)