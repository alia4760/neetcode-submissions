class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [c.lower() for c in s if c.isalnum()]
        if clean_s == clean_s[::-1]:
            return True 
        else:
            return False
        