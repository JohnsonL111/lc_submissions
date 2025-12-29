class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # nums.sort()
        # for i in range(0, n+1):
        #     if i == n:
        #         return i
        #     elif i != nums[i]:
        #         return i
        
        expect = sum(i for i in range(0, len(nums)+1))
        actual = sum(x for x in nums)
        return expect - actual