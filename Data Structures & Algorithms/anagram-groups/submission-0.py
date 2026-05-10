from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            # items converts it to (e,1), (t,1) ...
            #converts to a sorted tuple
            key = tuple(sorted(Counter(word).items())) 
            groups[key].append(word)
        return list(groups.values())

        