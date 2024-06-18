# 633. Sum of Squared Numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        div = 2    # Smallest prime number
        while (div * div <= c):
            if (c % div == 0): # div is a factor of c
                expCount = 0

                while (c % div == 0): # increment the exponent of div
                    expCount += 1
                    c /= div

                if (div % 4 == 3) and (expCount % 2 != 0): # check power of prime factor
                    return False
            div += 1
        return (c % 4 != 3)
