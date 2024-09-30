class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1,n):
            for g in range(i+1,n):
                temp = g**2 + i**2
                _temp = int(sqrt(temp))
                if _temp*_temp == temp and _temp <= n:
                    res+=2
        return res
        