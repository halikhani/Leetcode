# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:
        ans = []
        for i in range(len(s)):
            if i == 0:
                if int(s[i]) == 0:
                    return 0            # corner case when the string starts with zero
                else:
                    ans.append(1)
            else:
                cur_num = int(s[i])
                prev_num = int(s[i-1])
                
                # if both digits are zero: not valid and should return zero
                # if prev_num is zero and cur_num is non-zero: same ans as prev one
                # elif prev_num is non-zero and cur_num is zero: two digits should be less than 26 otherwise its not                 # gonna be a possible outcome
                # else: either two last digits make a valid comb or not, and based on that, calc the new ans
                if prev_num == 0 and cur_num == 0:
                    return 0
                if prev_num == 0 and cur_num != 0:
                    ans.append(ans[-1])
                elif prev_num != 0 and cur_num == 0:
                    # s[i-1:i+1] should be a valid encoding which is less than 26 otherwise the whole string is not                     valid
                    if int(s[i-1:i+1]) > 26:
                        return 0
                    else:
                        if i < 2:
                            ans.append(1)
                        else:
                            ans.append(ans[-2])
                else:
                    if int(s[i-1:i+1]) <= 26:
                        if i < 2:
                            ans.append(2)
                        else:
                            ans.append(ans[-1] + ans[-2])
                    else:
                        ans.append(ans[-1])
        return ans[-1]
                