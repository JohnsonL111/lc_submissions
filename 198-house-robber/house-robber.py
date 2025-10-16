class Solution:
    def rob(self, nums: List[int]) -> int:
        # global max amount of money = best you can do inc/ex current house
        # bottom up
        dp = [0] * (len(nums)+1)
        dp[0]=0
        dp[1]=nums[0]

        # build table
        for i in range(2, len(dp)):
            skip = dp[i-1]
            rob = dp[i-2] + nums[i-1]
            dp[i] = max(skip, rob)


        return dp[len(nums)]

        