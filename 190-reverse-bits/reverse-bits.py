class Solution:
    def reverseBits(self, n: int) -> int:
        # when calculating the bit version of n dont reverse it when reading up. Instead just read down
        # convert that bit rep into a number

        bits = 32*[0]
        idx = 0

        while n > 0:
            if n % 2 != 0:
                bits[idx] = 1
            idx += 1
            n //= 2
        
        bit_string = "".join(str(x) for x in bits)

        return int(bit_string, 2)
        

        