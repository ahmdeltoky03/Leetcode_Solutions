class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        _list = []
        char_num1 ={}
        n = len(nums1)
        for i in range(n):
            if nums1[i] in char_num1:
                char_num1[nums1[i]] += 1
            else:
                char_num1[nums1[i]] = 1

        m = len(nums2)
        for i in range(m):
            if nums2[i] in char_num1 and char_num1[nums2[i]]>0:
                    _list.append(nums2[i])
                    char_num1[nums2[i]] -= 1
        return _list