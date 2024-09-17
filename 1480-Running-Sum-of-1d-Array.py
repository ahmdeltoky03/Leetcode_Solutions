class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _list = []
        _sum = 0
        for num in nums:
            _sum += int(num)
            _list.append(_sum)
        return _list