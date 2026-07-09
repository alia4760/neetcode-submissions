class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = collections.Counter(s1)
        if len(s1) > len(s2):
            return False
        l = 0
        counter = {}
        for r in range(len(s2)):
            counter[s2[r]] = counter.get(s2[r],0) + 1
            if r-l+1 < len(s1):
                continue
            else:
                if s1_counter == counter:
                    return True 
                counter[s2[l]] -= 1
                if counter[s2[l]] == 0:
                    del counter[s2[l]]
                l+=1
        return False



            

        