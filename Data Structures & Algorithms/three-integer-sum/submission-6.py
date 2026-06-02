class Solution:
    def threeSum(self, numbs: List[int]) -> List[List[int]]:
        nums = sorted(numbs)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1
             
            while left < right:
                current_num = nums[i] + nums[left] + nums[right]
                if current_num > 0:
                    right-=1
                elif current_num < 0:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1

        
        return res
