# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution(object):
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def is_in_range(x):
            if x > (2**31 - 2) or x < ((-1)*(2**31)):
                return False
            return True
    
        if x >=0:
            s = str(x)
            s_rev = s[::-1]
            if is_in_range(int(s_rev)):
                return int(s_rev)
            return 0
        else:
            s = str(x)[1:]
            s_rev = s[::-1]
            i_rev = (-1)*(int(s_rev))
            if is_in_range(i_rev):
                return i_rev
            return 0
            
        