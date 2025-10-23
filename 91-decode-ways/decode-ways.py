class Solution:
    def numDecodings(self, s: str) -> int:
        #1-26
        # encoding int to strings
        # 11106 -> AAJF (1, 1, 10, 6) or KJF (11, 10, 6)
        # dp[i] = # ways to decode s[:i] (i-1 chars)
        n = len(s)
        dp = [0] * (n+1)

        # base cases
        dp[0] = 1 # 1 way to decode empty string ( do nothin)
        dp[1] = 0 if s[0] == '0' else 1 # '0' has no mapping

        # looking at prefix s[:i]
        # EXAMPLE: s = "226"
        for i in range(2, n+1):
            # add single digit to end (6)
            # "2 2 6"  → BBF
            # "22 6"   → VF
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            # add double digit to end (26)
            # "2 26" → BZ
            # check from [a,b)
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]
            





        