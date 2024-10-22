class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            flag = True
        
            
        total = 0
        num = x
        while x > 0 :#121
            temp = x % 10
            total= total*10 + temp
            x //= 10
        if total == num:
            flag = True
        else:
            flag = False
        return flag
        
#obj = Solution()
#print(obj.isPalindrome(int(12321)))