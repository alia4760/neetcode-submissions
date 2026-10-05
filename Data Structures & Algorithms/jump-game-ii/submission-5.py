class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        edge = 0
        for i in range(len(nums)-1):
            farthest = max(i+nums[i], farthest)
            if i == edge:
                edge = farthest
                jumps+=1

        return jumps 