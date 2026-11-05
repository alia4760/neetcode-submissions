import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = math.ceil(sum(piles) / h)
        high = max(piles)

        while low <= high: 
            k = (low+high)//2 
            time = sum([math.ceil(pile/k) for pile in piles])
            if time <= h:
                high = k - 1
            else:
                low = k + 1
        
        return low 
