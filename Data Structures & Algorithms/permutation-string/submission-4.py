class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counter = collections.Counter(s1)
        counter = {}
        l = 0
        for r in range(len(s2)):
            counter[s2[r]] = counter.get(s2[r], 0) + 1
            if r - l + 1 == len(s1):
                if counter == s1_counter:
                    return True
                counter[s2[l]] -= 1
                if counter[s2[l]] == 0:
                    del counter[s2[l]]
                l += 1
        return False