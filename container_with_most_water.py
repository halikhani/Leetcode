# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        l, r = 0, len(height)-1
        
        while l < r:
            min_h = min(height[l], height[r])
            area =  min_h* (r-l)
            max_area = max(max_area, area)
            
            # how to slide the window: move the pointer that is limiting the area (the min between l and r)
            if height[l] == min_h:
                l += 1
            else:
                r -= 1
        return max_area