class Solution(object):
    def reverse(self, x):
        \\\
        :type x: int
        :rtype: int
        \\\
        flag = True
        if x < 0 :
            flag = False
            x = -x
        reversed_x = int(str(x)[::-1])
        if reversed_x >= (2**31)-1:
            return 0
        return reversed_x if flag else -reversed_x
        