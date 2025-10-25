class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min # of coins to make up i
        # set to inf at first
        dp = [float('inf')] * (amount+1)
        # base case
        dp[0] = 0

        for i in range(1, len(dp)):
            # for each coin
            for c in coins:
                # can use the coin
                if i - c >= 0:
                    # initially dp[i] is inf
                    # +1 to add the coin
                    dp[i] = min(dp[i], dp[i-c] + 1)


        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]



