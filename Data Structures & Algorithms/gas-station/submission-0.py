class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = 0
        start_point = 0
        balance = 0
        for i in range(len(gas)):
            fuel += (gas[i]-cost[i])
            balance += gas[i] - cost[i]
            if fuel >= 0:
                pass
            else: 
                fuel = 0
                start_point = i+1 
        
        if balance >= 0:
            return start_point 
        else:
            return -1
                


           