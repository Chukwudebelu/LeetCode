class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s);
        if n < 4 or n > 12:
            return []
        elif n == 4:
            return ['.'.join(list(s))]
        elif n == 12:
            lst = []
            for i in range(0,12,12//4):
                if s[i] != '0':
                    if int(s[i:i+3]) <= 255:
                        lst += [s[i:i+3]]
                else:
                    break
            return ['.'.join([num for num in lst])] if len(lst) == 4 else []
        else: # 5,6,7,8,9,10,11
            lst1 = []
            x = lambda s: s == str(int(s)) and int(s) <= 255
            for i in range(1,n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                        if x(a) and x(b) and x(c) and x(d):
                            lst1.append(a + '.' + b + '.' + c + '.' + d)
            return lst1
