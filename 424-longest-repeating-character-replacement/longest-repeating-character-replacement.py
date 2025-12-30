class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we are given k letter transformations 
        # we want to find a substring where after k transformations it has the most consecutive chars
        # maintain a window between L and R pointer to form a substring
        # create a hashmap from the chars in that substring which is our possible transformation values and their counts.
        # EX: substring= "ABB" then hm = {A: 1, B:2}
        # we want to see if we can transform it into "BBB" so we use the most frequent char as our transformation char.
        # its successfully transformable (can become BBB) if length of substring - count of B <= k
        # we want to see that for k transofmrations using the set as the input can we make the substring all consecutive characters. If we can then compare its length vs a previous successful substring.

        l, r = 0, 0
        maxLength = 0
        end = len(s)-1
        count = defaultdict(int)

        while r <= end:
            char = s[r]
            count[char] += 1
            numTransformNeeded = (r-l+1) - max(v for v in count.values())
            # shrink window to become valid (impossible transform)
            while numTransformNeeded > k:
                charRemove = s[l]
                l+=1
                count[charRemove] -=1
                numTransformNeeded = (r-l+1) - max(v for v in count.values())

            # valid window now
            if numTransformNeeded <= k:
                maxLength = max(maxLength, r-l+1)
            r+=1

        return maxLength




     