class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # we want to find the longest consecuive chains of 1s possible given k transformations
        # we should maintain a window bounded by L and R pointers where we are moving the R pointer at each iteration
        # we should maintain the count of 0s seen in a window
        # for valid windows we want to see if we can flip the 0s in the window into 1s which is possible if k >= num of 0's
        # for invalid windows we want to shrink the window from the left
        # return the maximum length of chain of 1s found in a window

        l, r = 0, 0
        maxLen = 0
        end = len(nums)-1
        numZeroes = 0

        while r <= end:
            # invalid window
            numOnes = (r-l+1) - numZeroes
            numZeroesNeeded = (r-l+1) - numOnes
            while k < numZeroesNeeded:
                if nums[l] == 0:
                    numZeroes -= 1
                l+=1
                numOnes = (r-l+1) - numZeroes
                numZeroesNeeded = (r-l+1) - numOnes
            # valid window
            if nums[r] == 0:
                numZeroes += 1

            numOnes = (r-l+1) - numZeroes
            numZeroesNeeded = (r-l+1) - numOnes
            # check if chain is possible
            if k >= numZeroesNeeded:
                maxLen = max(maxLen, r-l+1)
            r+=1

        return maxLen