class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # need a right and left pointer that create a window that is a substring of s
        # create a static hashmap based on p and their counts (does not change)
        # we need to slide the right pointer across s.
        # keep updating a hashmap of the counts of seen characters in s
        # when the size of the window is the same as the length of p then check if p is an anagram of the current window. If yes then add the right pointer to the list to return.
        # when the size of the window is more than the length of p then slide the left pointer
        # when the right pointer gets to the last valid index in s then return the list of indexes
        #  s = "cbaebabacd", p = "abc"

        l, r = 0,0
        count_p = Counter(p)
        count_s = defaultdict(int)
        len_p = len(p)
        end = len(s)-1
        idxs = []

        while r <= end:
            char = s[r]
            count_s[char] += 1
            # invalid window
            while r-l+1 > len_p:
                char_remove = s[l]
                count_s[char_remove]-=1
                if count_s[char_remove] == 0:
                    del count_s[char_remove]
                l+=1

            # valid window
            if r-l+1 == len_p:
                if count_s == count_p:
                    idxs.append(l)
            r+=1
            
        return idxs

