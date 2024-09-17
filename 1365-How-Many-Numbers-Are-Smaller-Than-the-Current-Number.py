class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt_list = []
        cnt = 0
        for i in range(len(nums)):
            cnt = 0
            for g in range(len(nums)):
                if nums[g] < nums[i] and i!=g:
                    cnt += 1
            cnt_list.append(cnt)
        return cnt_list