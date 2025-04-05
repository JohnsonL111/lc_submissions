class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we know how to find anagrams via the Counter method or ord(c)-ord('a')
        # we cant use a dict as a key so use a tuple

        # tuple of the sorted counts of each char: original string
        countStrs = {}
        for s in strs:
            countS = Counter(s)
            key = tuple(sorted(countS.items()))
            if key not in countStrs:
                countStrs[key] = []

            countStrs[key].append(s)
        
        listAnagrams = []
        for v in countStrs.values():
            listAnagrams.append(v)

        return listAnagrams




                

