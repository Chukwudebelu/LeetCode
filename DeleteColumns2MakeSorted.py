# 944. Delete Columns to Make Sorted
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if len(strs[0]) == 0:
            return 0
        elif len(strs[0]) == 1:
            for i in range(len(strs)-1):
                if strs[i] > strs[i+1]:
                    return 1
                else:
                    return 0
        else:
            elem = lambda x, i, j: x[i][j]
            lst2 = []
            for k in range(len(strs[0])):
                lst = []
                for j in range(len(strs)):
                    lst.append(elem(strs,j,k))
                lst2 += [lst]
            things = map(''.join,lst2)
            count = 0
            for chars in things:
                chars_sort = ''.join(sorted(chars))
                if chars != chars_sort:
                    count += 1
            return count
