class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # optimized approach: apply 2sumII helper n times 
        # o(nlogn) to sort - 2ptr only works on sorted input
        # o(n) worst case for initial scan and at each scan index call the helper which is worst case o(n) comparisons
        # total o(n^2) time
        
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(0, n):
            # since its sorted if nums[i] > 0 then cannot sum to 0
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                # check for three sums possible with i + 2 nums from [i+1:n]
                self.threeSumHelper(nums, i, res)
        return res

    # from i to end of nums try to find a three sum using 2 ptr
    def threeSumHelper(self, nums, i, res):
        l = i +1
        r = len(nums)-1

        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1 # try to increase
            elif sum > 0:
                r -=1 # try to decrease
            else:
                res.append([nums[i], nums[l], nums[r]])

                # move both pointers once
                l += 1
                r -= 1

                # skip duplicates on next chek
                while l < r and nums[l] == nums[l-1]:
                    l += 1





                        

        
        
        