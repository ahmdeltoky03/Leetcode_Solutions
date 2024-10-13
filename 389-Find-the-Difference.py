class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == 0 :
            return t
        elif len(t) == 0:
            return s
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        n = min(len(s),len(t))
        for i in range(n):
            if s[i] != t[i] and len(s) > len(t):
                return s[i]
            if s[i] != t[i] and len(t) > len(s):
                return t[i]
        
        if len(s) > len(t):
            return s[n]
        else :
            return t[n]