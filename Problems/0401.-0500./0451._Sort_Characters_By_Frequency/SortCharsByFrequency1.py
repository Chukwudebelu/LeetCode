# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = dict()

        # Count the frequencies of each character
        for char in s:
            char_count[char] = char_count.get(char,0) + 1

        final_string = ""
        maps = list(char_count.items())
        maps.sort(key = lambda x: x[1])

        for i, _ in maps:
            final_string += i *char_count[i]
        return final_string[::-1]
