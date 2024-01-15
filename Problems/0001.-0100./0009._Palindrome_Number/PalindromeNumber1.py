# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Reverse the input number
        if (x < 0): return False
        else: # x > 0
            # Reverse the input number
            original_num, reverse_num = x, 0
        
            while (x):
                digit = x % 10  # Get last digit
                reverse_num = reverse_num*10 + digit # Shift by 1 order of magnitude
                x //= 10    # Go to next higher place value digit
            return (original_num == reverse_num)

    '''
    def signum(self, x: int) -> int:
        """
        Return the sign of x
        """
        return (-1 if (x < 0) else (0 if (x == 0) else 1))
    '''
