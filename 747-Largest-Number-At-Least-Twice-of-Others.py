class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        i = 0
        for num in nums:
            dic[num] = i
            i+=1
        nums.sort()
        return dic[nums[-1]] if nums[-1] >= 2*nums[-2]  else -1