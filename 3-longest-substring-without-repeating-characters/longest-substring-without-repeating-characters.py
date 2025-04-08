class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        longest = 0
        curr = set() # keeps track of current longest substring

        n = len(s)
        for r in range(n):
            c = s[r]
            if c in curr:
                while c in curr:
                    curr.remove(s[l])
                    l += 1
            # add it
            curr.add(s[r])
            # r += 1 # this auto gets incremented
            
            longest = max(longest, r-l+1)
        return longest


