class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while(num>0):
            if num%2 != 0:
                step+=1
                num -= 1
                if num == 0:
                    break
                step += 1
            else:
                step+=1
            num //= 2
        return step