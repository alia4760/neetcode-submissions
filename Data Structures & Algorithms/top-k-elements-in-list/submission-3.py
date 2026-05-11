from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_count_dict = defaultdict(int)
        for num in nums:
            int_count_dict[num] += 1

        sorted_value_list = sorted(list(int_count_dict.values()), reverse=True)
        
        result = []
        for key, values in int_count_dict.items():
            if values in sorted_value_list[0:k]:
                result.append(key)
        return result

        
        


        