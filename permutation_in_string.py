# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.

class Solution:
    
    def get_freq(self, s):
        sub_dict = dict()
        for c in s:
            sub_dict[c] = 1 + sub_dict.get(c, 0)
        
        return sub_dict
    
    def update_sub_dict(self, s_dict, remove_char, add_char):
        s_dict[remove_char] -= 1    # we are sure that remove_char has at least one count in its dict
        if s_dict[remove_char] == 0:
            del s_dict[remove_char]
        s_dict[add_char] = 1 + s_dict.get(add_char, 0)
        return s_dict
        
    def is_equal(self, sub1, sub2):
        return sub1 == sub2
    
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # create dict for s1
        s1_dict = self.get_freq(s1)
        sub_s2_dict = None
        for i in range(len(s2) - len(s1) + 1):
            sub_s2 = s2[i:i+len(s1)]
            if i == 0:
                sub_s2_dict = self.get_freq(sub_s2)
            else:
                sub_s2_dict = self.update_sub_dict(sub_s2_dict, s2[i-1], sub_s2[-1])
            
            if self.is_equal(s1_dict, sub_s2_dict):
                return True
        return False
        