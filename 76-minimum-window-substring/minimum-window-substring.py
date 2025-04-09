class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        n = len(s)
        r = 0
        bestMatch = ""
        countS = Counter()
        countT = Counter(t)

        def equalCount(countS, countT):
            for char in countT:
                if countS[char] < countT[char]:
                    return False
            return True

        for r in range(n):
            countS[s[r]] += 1
            # valid, but we want to look for the min window so shrink
            while equalCount(countS, countT):
                # update bestMatch
                if bestMatch == "" or (r - l + 1) < len(bestMatch):
                    bestMatch = s[l:r+1]

                countS[s[l]] -= 1
                l += 1
        return bestMatch

        