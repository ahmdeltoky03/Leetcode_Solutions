class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += abs(s.find(s[i])-t.find(s[i]))
        return res