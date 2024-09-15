class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = False
        for char in s:
            if char == 'b':
                flag = True
            elif char == 'a' and flag :
                return False
        return True
        