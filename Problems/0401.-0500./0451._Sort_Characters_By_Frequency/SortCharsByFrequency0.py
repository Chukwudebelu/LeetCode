# 451. Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = {}

        # Count the frequencies of each character
        for char in s:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        sorted_string = str()
        item_counts = sorted(freqs.items(), key = lambda x: x[1], reverse = True)
      
        # Empty string for output
        for char, count in item_counts:
            sorted_string += (char*count)
        return sorted_string
