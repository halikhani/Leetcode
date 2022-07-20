# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 
# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reversed_words = []
        for w in words:
            reversed_words.append(w[::-1])
            
        return ' '.join(reversed_words)
        