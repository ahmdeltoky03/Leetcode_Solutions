class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        res = 0
        i,g,k=0,0,0
        while (i<len(nums1) and g<len(nums2)):
            if nums1[i]<=nums2[g]:
                nums3.append(nums1[i])
                i+=1
            else :
                nums3.append(nums2[g])
                g+=1
            k+=1
        while i<len(nums1):
            nums3.append(nums1[i])
            k+=1
            i+=1
        while g<len(nums2):
            nums3.append(nums2[g])
            k+=1
            g+=1
        sze = len(nums1)+len(nums2)
        if sze % 2 != 0:
            _res = sze//2
            res = float(nums3[_res])
        else :
            _res = sze//2
            res = (nums3[_res]+nums3[_res-1])/2.0
        return res    

        
        