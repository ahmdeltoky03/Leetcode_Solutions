class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _list = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                _list.append(i)
        return _list
        