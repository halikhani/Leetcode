# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # got help from neetcode for this problem
        res = None
        max_len = 0
        
        for i in range(len(s)):
            # using l and r pointers
            # odd len answers
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            # even len answers, we just have to start l and r in diff indices
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res