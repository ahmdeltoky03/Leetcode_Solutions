class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        monInc = 0
        monDec = 0
        n = len(nums)
        for i in range(0,n-1):
            if nums[i+1]>=nums[i]:
                monInc += 1
            if nums[i+1]<=nums[i]:
                monDec += 1
        if monDec == n-1 or monInc == n-1:
            return True
        else:
            return False

        