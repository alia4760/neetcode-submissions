from collections import defaultdict 

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        l = 0 
        arr = self.dic[key] 
        r = len(arr) - 1 
        
        while l <= r: 
            mid = (l+r)//2 

            if arr[mid][0] > timestamp:
                r = mid - 1
            elif mid+1 > len(arr)-1:
                return arr[mid][1]
            elif arr[mid][0] <= timestamp and arr[mid+1][0] <= timestamp:
                    l = mid + 1
            else:
                return arr[mid][1]
        return ""


        
