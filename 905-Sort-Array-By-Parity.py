class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_num = []
        even_num = []
        for i in range(len(nums)):
            if nums[i] %2==0:
                even_num.append(nums[i])
            else:
                odd_num.append(nums[i])
        even_num.sort()
        odd_num.sort()
        _list = []
        for num in even_num:
            _list.append(num)
        for num in odd_num:
            _list.append(num)
        return _list
