class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_dict = {0: -1}
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            remainder = current_sum % k
            
            if remainder in remainder_dict:
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                remainder_dict[remainder] = i
        
        return False
