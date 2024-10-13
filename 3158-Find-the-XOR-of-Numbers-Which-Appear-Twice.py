class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _list = []
        res = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 2 and _list.count(nums[i]) == 0:
                _list.append(nums[i])
        # if len(_list) == 0:
        #     return 0
        for i in range(len(_list)):
            res ^= _list[i]
        return res

        