import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)

        while low <= high: 
            k = (low+high)//2 
            time = sum([math.ceil(pile/k) for pile in piles])
            if time <= h:
                high = k - 1
            else:
                low = k + 1
                k = low
        
        return k 
