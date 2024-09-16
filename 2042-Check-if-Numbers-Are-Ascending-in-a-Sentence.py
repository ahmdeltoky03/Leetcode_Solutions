class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.split()
        # lst = []
        flag = 1
        number = -1
        for letter in s:
            if letter.isdigit():
                if int(letter) > number:
                    number = int(letter)
                else:
                    flag = 0
                    break
        return flag
        