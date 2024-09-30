class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        _list = []
        for i in range(n):
            _list.append(nums[i])
            _list.append(nums[n+i])
        return _list
        