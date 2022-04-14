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
        
        def check_size(s, max_size):
            if len(s) > max_size:
                return len(s)
            return max_size
        
        def get_not_repeated_sub(s, occur_idx):
            if occur_idx == len(s) - 1 :
                return ''
            else:
                return s[occur_idx + 1:]
        
        current_substring = ''
        max_len = 0
        
        for i in s:  
            if i not in current_substring:
                current_substring += i
                
            else:
                occur_idx = current_substring.rfind(i)
                current_substring = get_not_repeated_sub(current_substring, occur_idx)
                current_substring += i
            
            max_len = check_size(current_substring, max_len)
        
        return max_len