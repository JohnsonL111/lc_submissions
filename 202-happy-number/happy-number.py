class Solution:
    def isHappy(self, n: int) -> bool:
        # 21 -> 2^2 + 1^2 = 5
        # 5 -> 5^1 = 5
        # 21 is NOT happy
        currVal = n
        count = 0
        while currVal != 1:
            if count == 10:
                return False # took too long
            lastVal = currVal
            currVal = 0
            for num in list(str(lastVal)):
                print(num)    
                currVal += pow(int(num), 2)

            print(f"lastVal is {lastVal}")
            print(f"currVal is {currVal}")
            count += 1
        
        return True # if reaches this point then currVal == 1 (happy)
        
        # n = 19
        # currVal = 19 | lastVal = 19 currVal = 1^2 + 9^2 = 82 |currVal != lastVal


            

        