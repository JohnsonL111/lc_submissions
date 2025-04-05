class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lower case it + remove alphaneumric
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        n = len(cleaned)
        idx = n-1
        for i in range(n):
            if cleaned[i] != cleaned[idx]:
                return False
            idx -=1
        return True
