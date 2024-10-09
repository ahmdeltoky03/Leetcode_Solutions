class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        ln = len(nums)
        while i<ln:
            if nums[i] == 0:
                temp = nums[i]
                nums.remove(nums[i])
                nums.append(temp)
            
            i+=1
        return nums
        