class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums first (2 pointer only works on sorted input)
        # do a linear scan on nums
        # for each index call a method to scan from [i+1:n] and [n:i+1]
        # in the method check if nums[i] + nums[l] + nums[r] is the closest to the target
        # if it is then update a value that tracks that.
        nums = sorted(nums)
        n = len(nums)
        closest = float('inf')

        for i in range(0, n):
            closest = self.closestScanHelper(i, nums, target, closest)

        return closest
    
    def closestScanHelper(self, i: int, nums: List[int], target: int, closest: int) -> int:
        n = len(nums)
        l = i+1
        r = n-1

        # scan from i+1 to n-1 (left) and n-1 to i+1 (right)
        while l < r:
            sumTriplet = nums[i] + nums[l] + nums[r]

            diff = abs(target - sumTriplet)
            diffBestSoFar = abs(target - closest)
            if diff < diffBestSoFar:
                closest = sumTriplet

            # increase sumtriplet
            if sumTriplet < target:
                l+=1
            elif sumTriplet > target:
                r-=1
            else:
                return closest # cant do better, return early to avoid tle

        return closest
        

        