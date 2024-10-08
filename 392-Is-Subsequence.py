class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx=0
        for char in t:
            if s_idx<len(s) and char==s[s_idx]:
                s_idx+=1
        return True if s_idx==len(s) else False