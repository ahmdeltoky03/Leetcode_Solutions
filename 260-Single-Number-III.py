class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        _list = []
        for i in range(len(nums)):
            x = nums.count(nums[i])
            if x == 1:
                _list.append(nums[i])
        return _list
        