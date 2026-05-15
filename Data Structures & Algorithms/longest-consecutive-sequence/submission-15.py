class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        longest = 0
        for num in nums:
            count = 1
            if num-1 not in nums:
                while num+1 in nums:
                    count+=1
                    num+=1
            longest = max(longest, count)  
        return longest



        