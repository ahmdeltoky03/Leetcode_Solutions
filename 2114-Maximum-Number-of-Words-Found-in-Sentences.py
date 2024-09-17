class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        res = 0
        # for sentence in sentences:
        #   numWord = 0
        #   for i in range(len(sentence)):
        #      if sentence[i] != ' ':
        #          numWord += 1
        # res = max(res, len(sentence)-numWord+1)
        for sentence in sentences:
            res = max(res,sentence.count(' '))
        return res+1
        