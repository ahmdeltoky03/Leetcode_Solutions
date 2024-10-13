class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        _num = sqrt(num)
        number = int(_num)
        return True if _num-number == 0 else False   
        