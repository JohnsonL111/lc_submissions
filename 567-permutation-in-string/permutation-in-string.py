class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # right and left pointer creating a window on s2
        # we slide the left pointer and check if the size of the current window is equal to the length of s1 (we can start seeing if its a valid permutation)
        # store a hashmap of the count of each character in the current window
        # then we have a hashmap of the counts of s1 (static) - create before we start sliding. Dont update it.
        # when the lengths match then compare the hashmaps. If s1 exists as a key in s2 then see the counts of it in s2. If the counts match the counts in s1 then return True.
        # slide the left pointer if the length of substring in s2 > length of s1
        # when we finish sliding across s2 (r ptr <= last idx in s2) then return False
        # s1 = "ab", s2 = "eidbaooo"

        l, r = 0, 0
        s1_count = Counter(s1)
        s2_count = defaultdict(int)
        s1_len = len(s1)
        end = len(s2)-1

        while r <= end:
            char = s2[r]
            s2_count[char] += 1
            # invalid window
            while s1_len < r-l+1:
                char_remove = s2[l]
                s2_count[char_remove] -=1
                if s2_count[char_remove] == 0:
                    del s2_count[char_remove]
                l+=1
            # valid window
            if s1_len == r-l+1:
                # check hashmaps
                if s1_count == s2_count:
                    return True
            r+= 1
            
        return False
        