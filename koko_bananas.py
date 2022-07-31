Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4


Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30


Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 106^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
Ac

class Solution(object):
    def get_hours(self, piles, k):
        result = 0
        for p in piles:
            result += ceil(p/k)
        return int(result)
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        if h == len(piles):
            return max(piles)
        else:
            l, r = 1, max(piles)
            res = r

            while r >= l:
                k = (l + r)//2
                # print('k:' + str(k))
                # print(piles)
                hours = self.get_hours(piles, k)
                # print('hours:')
                # print(hours)
                if hours <= h:
                    res = min(res, k)
                    r = k - 1
                else:
                    l = k + 1
            return res
            