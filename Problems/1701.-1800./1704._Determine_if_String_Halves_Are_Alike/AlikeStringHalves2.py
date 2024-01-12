class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = int(len(s)/2)
        left, right = s[0:half], s[half:len(s)]
        vowels = 'aeiouAEIOU'
        count_left, count_right = 0, 0

        for char1 in left:
            if char1 in vowels:
                count_left += 1

        for char2 in right:
            if char2 in vowels:
                count_right += 1
        
        return (True if (count_left == count_right) else False)
