class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        for i in range(len(nums)):
            removed = nums.pop(i)
            product = 1
            for num in nums:
                product *= num
            result.append(product)
            nums.insert(i, removed)
        return result