class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # take counter of each char
        countS = Counter(s)
        countT = Counter(t)

        # compare for counter equality
        return countS == countT