class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 0 
        l = len(heights)-1
        max_area = 0
        while r < l:
            smaller_h = min(heights[r],heights[l])
            length = l-r
            current_area = smaller_h*length

            if current_area > max_area:
                max_area = current_area

            if heights[r] >= heights[l]:
                l-=1
            elif heights[r] < heights[l]:
                r+=1
        return max_area
        