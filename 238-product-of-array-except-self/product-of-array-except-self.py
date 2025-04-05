class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix: product of all elements before an element
        # suffix: product of all eleemnts after an element

        n = len(nums)
        prefix = [1] * n
        product = 1
        for i in range(n):
            prefix[i] = product
            product *= nums[i]
        
        suffix = [1] * n
        product = 1
        for i in range(n-1, -1, -1):
            suffix[i] = product
            product *= nums[i]

        answer = []
        for i in range(n):
            answer.append(prefix[i] * suffix[i])
        return answer






        