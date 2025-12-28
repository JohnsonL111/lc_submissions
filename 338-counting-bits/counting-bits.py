class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n: int) -> int:
            hw = 0

            # odd number
            while n > 0:
                if n % 2 != 0:
                    hw+=1
                n //= 2

            return hw
        
        # make helper to calculate number of 1s. Append result to the array
        result = []
        for i in range(n+1):
            hw = countOnes(i)
            result.append(hw)
        return result

        
        