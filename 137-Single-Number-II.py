class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            x = nums.count(nums[i])
            if x == 1:
                return nums[i]
        