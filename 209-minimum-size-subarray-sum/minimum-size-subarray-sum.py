class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        ans = float('inf')

        for right, x in enumerate(nums):
            curr += x
            # shrink while valid to get the minimal window ending at `right`
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans