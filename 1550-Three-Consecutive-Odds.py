class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag=False
        for i in range(len(arr)-2):
            if (arr[i]%2 and arr[i+1]%2 and arr[i+2]%2):
                flag=True
                break
        
        return flag