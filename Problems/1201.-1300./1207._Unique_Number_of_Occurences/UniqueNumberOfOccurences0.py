# 1207. Unique Number of Occurences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_arr = {}

        for num in arr:
            dict_arr[num] = dict_arr.get(num, 0) + 1

        freqs, nums = [*set(dict_arr.values())], list(dict.keys(dict_arr))

        return len(freqs) == len(nums)
