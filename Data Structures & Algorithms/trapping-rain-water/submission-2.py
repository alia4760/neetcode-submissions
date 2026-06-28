class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        res = 0

        for i in range(1,len(height)):
            if max_left[i-1] < height[i]:
                max_left[i] = height[i]
            else:
                max_left[i] = max_left[i-1]
        
        for i in range(len(height)-2,-1,-1):
            if max_right[i+1] < height[i]:
                max_right[i] = height[i]
            else:
                max_right[i] = max_right[i+1]
        
        for i in range(len(height)):
            res += min(max_right[i], max_left[i]) - height[i]

        return res
        

