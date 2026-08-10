class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        height = min(bar1, bar2)
        dist = bar2idx - bar1idx 

        area = dist*height
        """ 
        l = 0
        r = len(heights) - 1
        max_area = -1
        while l < r:
            # calc area
            area = min(heights[l], heights[r]) * (r-l)
            # check against max area
            max_area = max(area, max_area)
            # move smaller bar
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return max_area