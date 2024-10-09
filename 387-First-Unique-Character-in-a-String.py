class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Use a dictionary to count the occurrences of each character
        char_count = {}
        
        # First pass to fill the dictionary with character counts
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Second pass to find the first unique character
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        return -1
