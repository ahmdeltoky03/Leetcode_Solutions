class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        _list = []
        # word_idx = {}
        # for i in range(len(words)):
        #     word_idx[words[i]]=i
        i = 0
        for word in words:
            if x in word:
                _list.append(i)
            i += 1
        return _list
        