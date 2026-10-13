import math 

class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append([val,val])
        elif val < self.arr[-1][0]:
            self.arr.append([val, val])
        else:
            minimum = self.arr[-1][0]
            self.arr.append([minimum, val])
        

    def pop(self) -> None:
        removed = self.arr.pop()

        

    def top(self) -> int:
        return self.arr[-1][-1]
        

    def getMin(self) -> int:
        return self.arr[-1][0]
        
