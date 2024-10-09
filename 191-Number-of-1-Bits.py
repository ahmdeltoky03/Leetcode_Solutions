class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        _n = bin(n)[2:]
        _n = list(_n)
        res = 0
        for i in _n:
            res += int(i)
        return res
        