class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = []
        results = [0] * len(temperatures)
        for i,t in enumerate(temperatures):

            while len(index) > 0 and t > temperatures[index[-1]]:
                removed = index.pop()
                results[removed] = i-removed
            
            index.append(i) 
        
        return results
                    
        