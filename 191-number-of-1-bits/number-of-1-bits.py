class Solution:
    def hammingWeight(self, n: int) -> int:
        # 8
        # 8 // 2 = 4 r 0
        # 4 // 2 = 2 r 0
        # 2 // 2 = 1 r 1
        # 1 // 2 = 0 r 0
        # 0100

        hw = 0 
        while n > 0:
            if n % 2 != 0:
                hw+=1
            n = n // 2
        return hw
        