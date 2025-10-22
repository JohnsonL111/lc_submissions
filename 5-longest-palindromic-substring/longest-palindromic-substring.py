class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check every substring and check if its a palindrome and return the longest one (brute force)
        # linear scan (n) for every substring (n^2)
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i #center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                 if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                 l -= 1
                 r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -=1
                r+= 1
        return res


        