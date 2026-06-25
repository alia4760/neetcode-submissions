class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = set()
        max_count = 0
        l,r = 0,0
        
        while r < len(s):
            if s[r] not in longest_substring:
                longest_substring.add(s[r])
                r+=1
                max_count = max(max_count,r-l)
            else:
                longest_substring.remove(s[l])
                l+=1
        return max_count


        