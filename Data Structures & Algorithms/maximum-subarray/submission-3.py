class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_total = nums[0]
        best_total = nums[0]

        for i in range(1,len(nums)):
            if current_total < 0:
                current_total = nums[i]
            else:
                current_total += nums[i]
            best_total = max(current_total, best_total)
            
            
        
        return best_total
            
        