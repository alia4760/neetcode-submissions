class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            message_str = "*?*$*".join(strs)
            return message_str  
        else:
            return "!!!!!"

    def decode(self, s: str) -> List[str]:
        if s == "!!!!!":
            return []
        else:
            message_arr = s.split("*?*$*")
            return message_arr
        
        
