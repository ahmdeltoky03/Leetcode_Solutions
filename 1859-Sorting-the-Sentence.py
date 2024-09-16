class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        dic_word = {}
        for word in s:
            dic_word[int(word[-1])] = word[:len(word) - 1]
        sort_dic = list(dic_word.keys())
        sort_dic.sort()
        strr = ""
        for word in sort_dic:
            strr += " "+dic_word[word]
        strr = strr[1:]

        
        return strr