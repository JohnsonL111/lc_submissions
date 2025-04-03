class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        found = False

        while not found:
            sumTwo = numbers[l] + numbers[r]
            if sumTwo > target:
                r -=1
            elif sumTwo < target:
                l += 1
            else:
                found = True

        return [l+1, r+1]

        
