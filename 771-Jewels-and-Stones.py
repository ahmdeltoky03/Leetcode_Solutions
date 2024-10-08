class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        n = len(stones)
        res = 0
        for i in range(n):
            if stones[i] in jewels:
                res += jewels.count(stones[i])
        return res
        