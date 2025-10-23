class Solution:
    def countSubstrings(self, s: str) -> int:
        # expand from center and go outwards 1 char at a time 
        start = 0
        last = len(s)
        count = 0

        for center in range(last):
            # odd (center is char)
            count += self.countPalindrome(s, center, center)

            # even (center is between char)
            count += self.countPalindrome(s, center, center+1)
        return count

    def countPalindrome(self, s, start, end) -> count:
        count = 0
        last = len(s)-1
        while (start >= 0 and end <= last and s[start] == s[end]):
            count += 1
            start -= 1
            end +=1
        return count



        
        