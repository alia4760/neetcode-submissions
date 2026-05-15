class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = collections.defaultdict()
        ideal_pair = []
        for i in range(len(nums)):
            ideal = target - nums[i]
            if ideal in dic:
                ideal_pair.extend([dic[ideal],i])
            dic[nums[i]] = i 
        return ideal_pair

            

