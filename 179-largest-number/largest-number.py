class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # a + b vs b + a
        # 30, 34, 9
        # 34309
        # 93430

        #a=9, b=34
        # a + b > b + a?
        # 934 > 349 True
        # put a before b

        # selection sort
        # loop through array, move smaller number to front
        # this is a variation of selection sort where we move the largest to the front
        numStr = list(map(str, nums)) # map returns a lazy iterator
        size = len(nums)
        for i in range(size):
            maxIdx = i
            for j in range(i+1, size):
                if numStr[j] + numStr[maxIdx] > numStr[maxIdx] + numStr[j]:
                    # a + b > b + a
                    # 9 + 30 > 30 + 9
                    maxIdx = j
            numStr[i], numStr[maxIdx] = numStr[maxIdx], numStr[i]

        # return 0 if largest num is 0
        if (numStr[0] == '0'):
            return '0'
        
        return ''.join(numStr)




        