class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l pointer ascends. start at beginning
        # r pointer descends. start at end.
        # Input: nums = [-4,-1,0,3,10]
        # [16,1,0,9,100]. When you square it the largest numbers appears first and last.
        # so we should populate an array from end (largest) to start (smallest)
        # Output: [0,1,9,16,100]


        l = 0
        r = len(nums)-1
        retSorted = [0] * len(nums)
        i = len(nums)-1

        while l <= r:
            l_squared = nums[l]*nums[l]
            r_squared = nums[r]*nums[r]

            if l_squared >= r_squared:
                retSorted[i] = l_squared
                l+=1
            else:
                retSorted[i] = r_squared
                r-=1
            i-=1

        return retSorted



        
                
