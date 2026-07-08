class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        change = k
        max_window = 0 
        for i in range(1,len(s)):
            sub_s = s[left:i+1]
            sub_counter = collections.Counter(sub_s)
            most_common_int = sub_counter.most_common()[0][1]
            sum_sub_counter = sum(sub_counter.values())
            if sum_sub_counter - most_common_int <= k:
                if max_window < len(sub_s):
                    max_window = len(sub_s)
            else: 
                left+=1
        
        return max_window
            


            