class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # without duplicate characters suggests we can use a set to hold our current substring
        # a set gives us o(1) access (hashset)
        # we want to maintain a window between L and R pointers and keep track of its length as it grows
        # we want to update a longest substring length variable as we grow the window
        # when there is a duplicate character at R we want to shrink from the left and remove the left character from the set until there are no duplicates
        # when our R pointer reaches the end of the string we can return the longest substrength length variable found

        l, r = 0, 0
        substring = set()
        longest = 0
        end = len(s)-1

        while r <= end:
            char = s[r]

            # char exists already
            while char in substring:
                char_remove = s[l]
                substring.remove(s[l])
                l+=1
            
            # no dupes at this point onwards
            substring.add(char)
            longest = max(len(substring), longest)
            r+=1

        return longest


