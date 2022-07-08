# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = None
        chars_list = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                chars_list.append(c)
            else:
                if c == ')':
                    if len(chars_list) == 0:
                        result = False
                        return
                    else:
                        if chars_list[-1] == '(':
                            del chars_list[-1]
                        else:
                            result = False
                            return
                if c == '}':
                    if len(chars_list) == 0:
                        result = False
                        return
                    else:
                        if chars_list[-1] == '{':
                            del chars_list[-1]
                        else:
                            result = False
                            return
                        
                if c == ']':
                    if len(chars_list) == 0:
                        result = False
                        return
                    else:
                        if chars_list[-1] == '[':
                            del chars_list[-1]
                        else:
                            result = False
                            return
                    
        result = True if len(chars_list) == 0 else False
        return result
                
            