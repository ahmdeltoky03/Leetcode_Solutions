class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(1,n):
            res = n*i 
            if res % 2 == 0:
                break
        return res if res != 1 else 2