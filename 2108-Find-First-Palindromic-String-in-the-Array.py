class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = ""
        for word in words:
            cnt = 0
            n = len(word)
            for i in range(n//2):
                if word[i]==word[len(word)-i-1]:
                    cnt += 1
            if cnt == len(word)//2:
                res = word
                break
        return res
        