# TODO: think of a better condition for returning the result

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:

# Input: n = 2
# Output: false
 
# Constraints:
# 1 <= n <= 231 - 1


class Solution(object):
    
    def get_square_sum(self, n):
        rem = n
        digits = []
        while rem != 0:
            digit = rem % 10
            digits.append(digit)
            rem = rem // 10
            
        result = 0
        for i in digits:
            result += (i**2)
            
        return result
            
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        square_sum = n
        iter_num = 0
        while square_sum != 1:
            square_sum = self.get_square_sum(square_sum)
            iter_num += 1
            if iter_num > 10:
                return False
        return True
                
        
        