class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        lst = []
        for c in s:
            if c in ["[","{","("]: 
                lst.append(c)
            elif c in mapping.keys():
                if not lst or lst[-1] != mapping[c]:
                    return False
                lst.pop()
        if lst:
            return False
        else: 
            return True  
                    
                


                
        

        