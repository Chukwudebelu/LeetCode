class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [*map(int,list(str(int(''.join([*map(str,digits)])) + 1)))]
