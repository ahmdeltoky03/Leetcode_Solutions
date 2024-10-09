class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t_index = 0
        
        for char in s:
            if t_index < len(t) and char == t[t_index]:
                t_index += 1
        return len(t) - t_index