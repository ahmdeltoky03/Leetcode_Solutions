class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        tmp = ""
        for word in words:
            tmp+=word
            if tmp == s:
                return True
            elif len(tmp) > len(s):
                return False
        return False