class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(0, n):
        #     val1 = nums[i]
        #     for j in range(i+1, n):
        #         if target - val1 == nums[j]:
        #             return [i, j]
                

        seen = {} # val:idx

        # update seen each iteration
        # loop once
        # calculate the needed val to hit the target
        # if that needed val is in seen you have the associated idx

        for k, v in enumerate(nums):
            needed = target - v
            if needed in seen:
                return [seen[needed], k]
            
            # add new entry to seen
            seen[v] = k
        




