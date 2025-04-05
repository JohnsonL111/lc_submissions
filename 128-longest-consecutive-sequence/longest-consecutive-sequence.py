class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # need to keep track of the longest consecutive sequence and return its length
        # only grow the longest consec seq if num-1 not in the set. So num is the start of a new seq
        # now you have a list of potential starting points
        # loop and keep track of the longest consec sequence
        numsSet = set(nums)

        starts = []
        for n in numsSet:
            if n-1 not in numsSet:
                starts.append(n)
        
        maxLen = 0
        for s in starts:
            currLen = 1
            while s+currLen in numsSet:
                currLen+=1
            maxLen = max(currLen, maxLen)
        
        return maxLen




        