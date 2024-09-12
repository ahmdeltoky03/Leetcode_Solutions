class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = int(s, 2)
        if num == 1:
            return 0
        res = 0
        while(num>0):
            if num % 2 != 0:
                res += 1
                num += 1
            else:
                res += 1
                num //= 2
                if num == 1:
                    break
               
        return res
        