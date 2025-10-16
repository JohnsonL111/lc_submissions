class Solution:
    def firstUniqChar(self, s: str) -> int:
        # try to do it with one pass of string

        # instnatiate Counter with the string
        freq = Counter(s)
        # loop string and first one with freq=1 return idx
        for idx, val in enumerate(s):
            if val in freq and freq[val] == 1:
                return idx
        return -1

        