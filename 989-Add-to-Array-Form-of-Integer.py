class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = ''.join(map(str, num))
        _num = int(s) + k
        _list = []
        while(_num):
            temp = _num % 10
            _list.insert(0,temp)
            _num /= 10
        return _list
        