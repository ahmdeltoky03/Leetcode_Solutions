class Solution(object):
    def maxArea(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        \\\
        [0,1,2,3,4,5,6,7,8]
        [1,8,6,2,5,4,8,3,7]
        \\\
        i = 0
        g = len(height) - 1
        maximum=0
        while i<=g:
            _width = g-i
            _height = min(height[i],height[g])

            area = _width*_height

            if area > maximum:
                maximum=area
            if(height[i]<height[g]):
                i+=1
            else:
                g-=1
        return maximum