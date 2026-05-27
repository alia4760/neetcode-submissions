class Solution:
    def threeSum(self, numbs: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(numbs, reverse=False)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            while left <= right:
                target = 0
                current_num = nums[left] + nums[right] + nums[i]
                if current_num == target and i!=right and right!=left and i!=left:
                    res.add((nums[left], nums[right], nums[i]))
                if current_num > target:
                    right -=1
                else:
                    left+=1
        return list(res)
        