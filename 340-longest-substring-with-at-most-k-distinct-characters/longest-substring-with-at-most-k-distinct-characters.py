class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # we need a variable to track the length of the longest substring that contains at most k distinct chars
        # we need right and left pointers to slide through this string
        # we need a hashmap to track the chars seen so far and their counts
        # while traversing the string we need to increment the count in the hash map
        # if len(keys) <= k then we want to update our "length of the longest substring variable"
        # if we do then we check the window size using r-l+1 and update our longest substring length
        # when we hit a violation we start removing from our hash map and incrementing the left pointer until its no longer a violation
        # increment the right pointer each time regardless

        longest = 0 # cant have neg length
        left, right = 0, 0
        hm = defaultdict(int)
        end = len(s)-1

        while right <= end:
            curr = s[right]
            hm[curr] += 1
            # fix if > k
            while len(hm) > k:
                remove = s[left]
                hm[remove] -= 1
                if hm[remove] == 0:
                    del hm[remove]
                left += 1
            # update longest after fixed
            longest = max(right - left + 1, longest)
            right += 1

        return longest


        