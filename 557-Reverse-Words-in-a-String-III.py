class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s = []
        s = s.split()
        for word in s:
            word = word[::-1]
            _s.append(word)

        _s = " ".join(_s)
        return _s

