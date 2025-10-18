class Solution:
    def rob(self, nums: List[int]) -> int:
        # split into two linear house robbing cases
        n = len(nums)
        # ---- edge cases ----
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # ---- helper for linear DP ----
        def rob_linear(arr):
            m = len(arr)
            dp = [0] * (m + 1)
            dp[0] = 0
            dp[1] = arr[0]
            for i in range(2, m + 1):
                rob = arr[i - 1] + dp[i - 2]
                skip = dp[i - 1]
                dp[i] = max(rob, skip)
            return dp[m]

        # ---- two cases ----
        case1 = rob_linear(nums[1:])   # skip first house
        case2 = rob_linear(nums[:-1])  # skip last house

        return max(case1, case2)