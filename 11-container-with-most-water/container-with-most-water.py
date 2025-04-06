class Solution:
    def maxArea(self, height: List[int]) -> int:
        # water = width * height
        n = len(height)
        r = n-1
        l = 0
        currMax = 0

        while l < r:
            # calculate the water
            w = r-l
            h = min(height[l], height[r])
            area = w * h
            currMax = max(area, currMax)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return currMax



