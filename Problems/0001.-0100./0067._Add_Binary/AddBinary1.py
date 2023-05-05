class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = [*map(self.bin2Decimal, [a, b])]
        c = a + b; bits = []
        if c == 0:
            return str(c)
        while c:
            bits += [str(c % 2)]
            c >>= 1
        return ''.join(bits[::-1])

    def bin2Decimal(self, x: str) -> int:
        num_x = 0
        for i in range(len(x)):
            num_x += int(x[-(i+1)])*(2**i)
        return num_x
