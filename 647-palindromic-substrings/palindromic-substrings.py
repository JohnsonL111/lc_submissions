class Solution:
    def countSubstrings(self, s: str) -> int:
        # i and j inclusive are start and end of substring
        n = len(s)
        dp = []
        count = 0
        # init dp of all False
        for i in range(n):
            dp.append([False] * n)
        rows = len(dp)
        cols = len(dp[0])
        print(f'max indexable is {rows - 1} and {cols - 1}')


        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        for i in range(n-1, -1, -1):
            # in first iteration its trivially s[-1] to s[-1]
            for j in range(i, n):
                # print(f'i {i} j {j}')
                # j-i <= 2 means no inner substring exist so skip dp lookup
                if s[i] == s[j] and  (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        
        return count

                
        




        
        