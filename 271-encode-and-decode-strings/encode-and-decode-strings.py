class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
    # list[str] -> str 
        # conver each value to its ordinal value then reconvert back
        # use # as a delimiter between each char in the string
        # use | as ad elimter between entires in the list
        encoded = ""
        for s in strs:
            for c in s:
                ordinal = ord(c)
                padded = str(ordinal) + "#"
                encoded += padded
            encoded += "|"
        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        finalList = []
        idx = 0
        n = len(s)
        currOrd = "" # per char
        decoded = "" # per string
        while idx < n:
            # need to decode the char
            while s[idx] != '|':
                if (s[idx] == '#'): # new char found
                    char = chr(int(currOrd))
                    decoded += str(char)
                    currOrd = "" # reset
                else:
                    currOrd += str(s[idx]) # keep incrementing to get the asci of the char
                idx += 1
            # string is found
            finalList.append(decoded)
            decoded = ""
            idx += 1

        return finalList

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))