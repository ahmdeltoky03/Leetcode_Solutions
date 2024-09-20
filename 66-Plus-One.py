class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(map(str, digits))
        num = int(s) + 1
        _list = []
        while(num):
            temp = num%10
            _list.insert(0,temp)
            num/=10
        return _list