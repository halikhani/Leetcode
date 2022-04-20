class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        
        l = 0
        r = len(height) - 1
        min_bar = min(height[l], height[r])
        max_area = (r - l)*min(height[l], height[r])
        current_area = 0
        
        while True:
            if l >= r-1 or max(height[l+1:r]) < min_bar:
                break
            else:
                if l == min_bar:
                    idx = l+1
                    while height[idx] < height[l]:
                        idx += 1
                    
                    new_min_bar = min(height[idx], height[r])
                    area = (r - idx)*(new_min_bar)
                    if area > max_area:
                        max_area = area
                    l = idx
                else:
                    idx = r-1
                    while height[idx] < height[r]:
                        idx -= 1
                    
                    new_min_bar = min(height[idx], height[l])
                    area = (idx - l)*(new_min_bar)
                    if area > max_area:
                        max_area = area
                    r = idx
            
       
            return max_area
                
                
        