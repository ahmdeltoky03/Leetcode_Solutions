class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        summ = 0
        prod = 1
        while(n):
            temp = n%10
            prod *= temp
            summ += temp
            n/=10
        res = prod - summ
        return res