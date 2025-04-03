class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: a string
        # output: length of longest substring without repeating chars

        # we want to make sure that l to r has non duplicate characters.
        # we do that by maintaining a set that contains the chars between l and r 

        l, r = 0, 0

        repeat = set()
        lenMax = 0

        while r <= len(s)-1:
            while (s[r] in repeat):
                repeat.remove(s[l])
                l += 1
            
            repeat.add(s[r])
            lenMax = max(lenMax, r-l+1)
            r +=1
        return lenMax

