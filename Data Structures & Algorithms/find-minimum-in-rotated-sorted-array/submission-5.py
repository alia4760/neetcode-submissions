import math 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        minimum = math.inf

        if r == 0:
            return nums[0]

        while l < r: 
            mid = (l+r)//2 
            #print(minimum, nums[mid], mid, l, r)
            
            if nums[mid] > nums[r]:
                l = mid + 1
                minimum = min(nums[l], minimum)
            else:
                r = mid
                minimum = min(nums[r], minimum)
        
       
        return minimum

            
        