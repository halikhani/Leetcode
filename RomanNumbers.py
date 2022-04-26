class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        exections = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        if num in exections.keys():
            return exections[num]

        ref_letters = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        ref_nums = list(ref_letters.keys())[::-1]
        result = ''
        remaining = num
        while remaining > 0:
            for e in ref_nums:
                if e <= remaining:
                    result += ref_letters[e]
                    remaining -= e
                    break

        return result

