class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # a valid substring needs to be exactly the same length as the entries in words concatenated
        # we need a window controlled by left and right pointers
        # we need a static counter of characters in words (frequency of each character) in a hash map
        # we need a hashmap to track the frequency of characters in s in our window that updates as we move our left and right pointer
        # a valid window is when the length of the window is the same as the length of entries concatenated - on a valid window check if it is a permutation of words if the counters match. Add the left index pointer
        # on an invalid window increment the left pointer
        # we increment the window as long as the right pointer doesn't exceed the last valid index in s

        if not s or not words:
            return []
        
        l, r = 0, 0
        word_len = len(words[0])
        len_c = word_len * len(words) 
        end = len(s) - 1
        count_w = Counter(words)      
        idxs = []

        while r <= end:
            # invalid window
            if r - l + 1 > len_c:
                l += 1

            # when window is exactly len_c, check if it's a valid concatenation
            if r - l + 1 == len_c:
                count_s = defaultdict(int)
                k = l
                # split s[l:r+1] into chunks of size word_len
                while k <= r:
                    word = s[k:k + word_len]
                    count_s[word] += 1
                    k += word_len

                # if word counts match target, record starting index
                if count_s == count_w:
                    idxs.append(l)

                # slide window forward by 1 so we can check the next position
                l += 1

            r += 1

        return idxs



        