# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len_str = len(strs[0])
        for str in strs:
            if len(str) < min_len_str:
                min_len_str = len(str)
        
        lcp = ''
        has_common_char = True
        for i in range(min_len_str):
            current_char = strs[0][i]
            for str in strs:
                if str[i] != current_char:
                    has_common_char = False
                    break
            if has_common_char is False:
                break
            else:
                lcp += current_char
        return lcp