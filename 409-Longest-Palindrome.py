class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        char_num = {}
        for char in s:
            if char in char_num:
                char_num[char] += 1
            else:
                char_num[char] = 1
        odd_occ = 0
        for char in char_num:
            if char_num[char] %2 ==0:
                 res += char_num[char]
            else:
                 res += char_num[char] - 1
                 odd_occ = 1

        return res+1 if odd_occ else res

        