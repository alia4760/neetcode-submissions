class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums_size = len(nums)-1
        index_tot = 0 
        for i in range(len(nums)):
            if i > index_tot:
                return False
            if index_tot >= nums_size:
                return True
                
            index_tot = max(i+nums[i],index_tot)
        
        return False 