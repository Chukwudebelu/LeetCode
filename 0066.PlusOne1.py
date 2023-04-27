class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Store the length of the array
        n = len(digits)
        # Get the integer from the array
        numFromDigits = 0 
        for i in range(n-1,-1,-1):
            numFromDigits += digits[i]*(10**(n-i-1))
        # Increment this integer by 1 (or You could have also declared numFromDigits to be 1 & skip this step)
        numFromDigits += 1
        # Initialize array to hold each new digit
        new_digits = []
        
        while (numFromDigits):
            n = numFromDigits % 10
            new_digits = [n] + new_digits
            numFromDigits //= 10
        return new_digits
        
