# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.    

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        current_s = ''
        max_sub_len = 0
        for c in s:
            if c not in current_s:
                current_s += c
            else:
                occur_idx = current_s.rfind(c)
                current_s = current_s[occur_idx+1:]
                current_s += c
            max_sub_len = max(max_sub_len, len(current_s))
        return max_sub_len