class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[k] != nums[j] and nums[i] != nums[j] and nums[k]!= nums[i]:
                        res+=1
        return res