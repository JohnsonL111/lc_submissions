class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # we need keep a variable that tracks the min length subarray whose sum is >= target
        # sliding window approach: we need right and left pointers
        # since we only have positive integers we know that if we add a value on the right it will always increase the size of the number
        # we could keep sliding the right pointer until its >= target
        # at that point we track its legnth using r-l+1 and check if its the smallest seen so far
        # and then we slide the left pointer until >= target breaks and check the length r-l+1 against the current tracked min length seen so far

        left, right = 0, 0
        end = len(nums)-1
        minLen = float("inf")
        currSum = 0
        while right <= end:
            currSum += nums[right]
            while currSum >= target:
                minLen = min(minLen, right-left+1)
                currSum -= nums[left]
                left+= 1
            right+= 1

        return minLen if minLen != float("inf") else 0