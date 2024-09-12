class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        res = 0
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                prev += 1
                res += prev - nums[i]
            else:
                prev = nums[i]

        return res
