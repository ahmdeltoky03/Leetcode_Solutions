class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            for g in range(i+1,n):
                if nums[i]==nums[g]:
                    res+=1
        return res 
        