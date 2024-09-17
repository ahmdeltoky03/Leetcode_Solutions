class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums1)):
            for g in range(len(nums2)):
                if (nums1[i] % (nums2[g]*k))==0:
                    cnt += 1 
        return cnt