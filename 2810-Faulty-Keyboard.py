class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        txt = ""
        for char in s:
            if char == 'i':
                txt = txt[::-1]
            else:
                txt+=char
        return txt
        