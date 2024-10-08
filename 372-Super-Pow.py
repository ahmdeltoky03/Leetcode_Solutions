class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        _sum = 0
        for i in range(len(b)):
            _sum = _sum*10 + b[i]
        res = pow(a, _sum,1337)
        return res
        
        