class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index_tot = len(nums) - 1
        target_index = 0
        for i in range(len(nums)):
            print(target_index)
            if i <= target_index:
                target_index = max(i+nums[i],target_index)
            if target_index >= index_tot:
                return True
        
        return False
            
            
            

            

        