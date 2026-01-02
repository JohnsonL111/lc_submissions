class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if the size of s > size of t then return empty string
        # we need a right and left pointer for creating a window between L and R
        # create a static Counter hashmap of t 
        # update a hashmap of the window as we parse through s
        # at every valid window (valid window is when the length of the window >= length of t)
        # constantly check the length of windows that are the same as t (track the minimum length substring found)
        # when the window is invalid and not a substring match, fix it by moving the left pointer until at least the size of the window >= length of t
        # when the right pointer goes past the last index then we are finished. Return the minimum length substring found.
        # s = "ADOBECODEBANC", t = "ABC"
        l, r = 0, 0
        end = len(s)-1
        count_t = Counter(t)
        count_s = defaultdict(int)
        smallest_substring = ""

        while r <= end:
            char = s[r]
            count_s[char] += 1
            # invalid window

            # valid window
            while all(count_s[k] >= v for k,v in count_t.items()):
                if smallest_substring == "" or r-l+1 < len(smallest_substring):
                    smallest_substring = s[l:r+1]

                char_remove = s[l]
                count_s[char_remove] -=1
                if count_s[char_remove] == 0:
                    del count_s[char_remove]
                l+=1
            
            r+=1

        return smallest_substring
                
