# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.

 
# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
#         # using extended Boyer-Moore approach
#         top_k = [None for i in range(k)]
#         top_k_counts = [0 for i in range(k)]
        
#         for n in nums:
#             if n in top_k:
#                 for i in range(k):
#                     if top_k[i] == n:
#                         top_k_counts[i] += 1
#                         break
#             else:
#                 for i in range(k):
#                     if top_k_counts[i] == 0:
#                         top_k[i] = n
#                         top_k_counts[i] = 1
#                         break
#                     if i == k - 1:
#                         for i in range(k):
#                             top_k_counts[i] -= 1
#         return top_k
            # didn't work! will think about it later
        
        # using a dict with keys to be counts and values to be numbers with that             count
        count_hits = dict()
        freqs = [[] for i in range(len(nums)+1)]
        for n in nums:
            count_hits[n] = 1 + count_hits.get(n, 0)

        for kk, v in count_hits.items():
            freqs[v].append(kk)

        top_k = []
        for i in range(len(freqs)-1, -1, -1):
            top_k += freqs[i]
        return top_k[:k]