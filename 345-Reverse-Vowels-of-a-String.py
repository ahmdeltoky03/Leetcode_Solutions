class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        for char in s:
            if char in ['a','i','e','o','u','A','E','I','O','U']:
                lst.append(char)
        lst = lst[::-1]
        i=0
        answer = ""
        for char in s:
            if char in ['a','i','e','o','u','A','E','I','O','U']:
                answer+=lst[i]
                i+=1
            else:
                answer+=char
        return answer