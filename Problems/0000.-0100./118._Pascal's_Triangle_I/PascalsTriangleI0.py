class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst2 = []
        for i in range(numRows):
            lst = []
            for j in range(i+1):
                lst.append(math.comb(i,j))
            lst2.append(lst)
        return lst2
