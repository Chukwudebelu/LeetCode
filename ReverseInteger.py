# 7. Reverse Integer
def reverse(self, x: int) -> int:
    if -9 <= x <= 9:
        return x
    str_int = str(x)
    if str_int[0] == '-':
        minus = '-'
        str_int = str_int[1:][::-1]
        while str_int[0] == '0':
            str_int = str_int[1:]
        str_int = minus + str_int
    else:
        str_int = str_int[::-1]
        while str_int[0] == '0':
            str_int = str_int[1:]
    ans = int(str_int) if -2**31 <= int(str_int) <= 2**31-1 else 0
    return ans
