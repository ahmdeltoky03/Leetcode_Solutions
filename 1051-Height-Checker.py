class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        _heights = [heights[i] for i in range(len(heights))]
        n = len(heights)
        heights.sort()
        cnt = 0
        for i in range(n):
            if _heights[i] != heights[i]:
                cnt+=1
        return cnt
        