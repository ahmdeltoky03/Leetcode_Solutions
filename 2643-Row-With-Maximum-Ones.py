class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        _list = [0, 0]
        maximum = 0
        row_num = 0
        for i in mat:
            lst = i
            cnt_1 = lst.count(1)
            if cnt_1 > maximum:
                maximum = cnt_1
                _list[0] = row_num//len(lst)
                _list[1] = cnt_1
            row_num += len(lst)
        return _list
        