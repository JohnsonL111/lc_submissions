class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n vertical lines
        # Area=(right index−left index)×min(height[left],height[right])
        # need to maximize the width and possible height combination

        l = 0
        r = len(height)-1
        maxArea = 0
        
        while (l < r):
            area = (r-l)*min(height[r], height[l])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                # move smaller height forward
                l += 1
            else:
                r -=1

        return maxArea