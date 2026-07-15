class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        else:
            l=0
            tracker = 0
            counter_t = collections.Counter(t)
            counter = {}
            smallest_sub = []
            for r in range(len(s)):
                counter[s[r]] = counter.get(s[r],0) + 1
                if counter_t.get(s[r],0) == counter[s[r]]:
                    tracker +=1 
                while tracker == len(counter_t):
                    canidate = s[l:r+1]
                    counter[s[l]] -= 1
                    l+=1
                    if not smallest_sub or len(canidate) < len(smallest_sub):
                        smallest_sub = canidate
                    if counter[s[l-1]] < counter_t.get(s[l-1], 0):
                        tracker -= 1
        
            return smallest_sub if len(smallest_sub) > 0 else ""