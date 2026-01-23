class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1 pass and update hash map with count of all numbers
        # 2nd pass to update with the numbers of each

        ht = defaultdict(int)
        for color in nums:
            ht[color] += 1
        
        n = len(nums)
        i = 0
        lastIdx = n-1
        # sort the keys (hardcode the colors)
        for color in (0,1,2):
            while ht[color] > 0:
                nums[i] = color
                ht[color] -=1
                i+=1
                
        


        