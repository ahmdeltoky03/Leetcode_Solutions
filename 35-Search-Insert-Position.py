class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        if target > nums[n-1] :
            return n
        for i in range(n):
            if nums[i] >= target:
                res = i
                break
        return res
    
        