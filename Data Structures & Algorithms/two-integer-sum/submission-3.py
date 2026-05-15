class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ideal_index = []
        for i in range(len(nums)):
            num = nums[i]
            ideal_num = target-num
            if ideal_num in nums: 
                ideal_position = nums.index(ideal_num)
                if ideal_position != i:
                    ideal_index.extend([i, ideal_position])
        
        return list(set(ideal_index))

