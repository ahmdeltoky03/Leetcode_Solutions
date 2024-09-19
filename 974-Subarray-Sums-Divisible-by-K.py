class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Dictionary to store the frequency of prefix sums mod k
        count = {0: 1}
        prefix_sum = 0
        res = 0
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            # if mod < 0:
            #     mod += k
            
            if mod in count:
                res += count[mod]
                count[mod] += 1
            else:
                count[mod] = 1
        
        return res
