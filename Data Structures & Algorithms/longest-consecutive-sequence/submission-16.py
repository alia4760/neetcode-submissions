class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums)
        for num in set_nums:
            count = 1
            if num-1 not in set_nums:
                while num+1 in nums:
                    count+=1
                    num+=1
            longest = max(longest, count)  
        return longest



        