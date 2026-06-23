class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        lst = []
        for c in s:
            if c in ["[","{","("]: 
                lst.append(c)
            elif c in mapping.keys():
                if mapping[c] not in lst:
                    return False
                last_c_lst = lst[-1]
                if mapping[c] == last_c_lst:
                    lst.pop()
        if lst:
            return False
        else: 
            return True  
                    
                


                
        

        