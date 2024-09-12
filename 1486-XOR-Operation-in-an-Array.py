class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start+2*i for i in range(n)]
        res = 0
        for i in range(n):
            res ^= nums[i]
        return res
        