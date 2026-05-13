import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1

        for i in range(len(nums)):
            prefix = nums[0:i] 
            suffix = nums[i+1:]
            prefix.extend(suffix)
            res = math.prod(prefix)
            result.append(res)
        
        return result
            