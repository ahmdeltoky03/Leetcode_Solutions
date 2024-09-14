class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        _list = []
        for i in range(len(arr2)):
            temp = arr1.count(arr2[i])
            while temp > 0:
                _list.append(arr2[i])
                temp -= 1
        arr1.sort()
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                _list.append(arr1[i])
        return _list