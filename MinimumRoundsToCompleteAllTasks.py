# 2244. Minimum Rounds to Complete All Tasks
def minimumRounds(self, tasks: List[int]) -> int:
        def twosThrees(n: int):
            # determines the numbers of 2s & 3s that adds up to make a number
            # n = 2*a + 3*b
            a, b = 0, 0
            if n % 3 == 0: # multiple of 3
                b = n //3
            else: # not a multiple of 3
                b = n // 3
                a = 0
                if n % 3 == 1:
                    a += 2
                    b -= 1
                elif n % 3 == 2:
                    a += 1
            return a+b if n != 1 else 0
        frequencies = Counter(tasks)
        rounds = 0
        for freq in frequencies.values():
            if freq == 1:
                return -1
            else:
                rounds += twosThrees(freq)
        return rounds
