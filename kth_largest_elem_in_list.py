# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maybe we can keep track of max k number of the stream so far and update that with each incoming number
        from heapq import heapify, heappush, heappop
        max_k = []
        heapify(max_k)
        for i, n in enumerate(nums):
            if i < k:
                heappush(max_k, n)
            else:
                min_in_k_max = heappop(max_k)
                if n < min_in_k_max:
                    heappush(max_k, min_in_k_max)
                else:
                    heappush(max_k, n)
        return max_k[0]
        
        
        
        # second solution
        # nums.sort()
        # return nums[len(nums) - k]

