class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        n = min(a,b)
        cnt =0
        for i in range(1,n+1):
            if a%i==0 and b%i==0:
                cnt+=1
        return cnt