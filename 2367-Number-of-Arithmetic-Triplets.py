class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[k]-nums[j] == diff and nums[j] - nums[i] == diff:
                        res+=1
        return res

        