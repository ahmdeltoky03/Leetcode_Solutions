class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        
        result = list(words[0])
        
        for word in words[1:]:
            new_result = []
            temp_result = list(result)
            for char in word:
                if char in temp_result:
                    new_result.append(char)
                    temp_result.remove(char)
            result = new_result
        
        return result
