# 654. Set Mismatch
class Solution:
    def findErrorNums(self, nums: list]) -> list]:
        min_num, max_num = 1, len(nums)
        s = [i for i in range(min_num, max_num+1)] # [1, 2, 3, ..., n]
        output = {j for j in s if j not in nums} # get the missing element
        
        duplicate = set()
        for k in nums:
            if (nums.count(k) == 2):
                duplicate.add(k)
            else:
                del k
        return list(duplicate) + list(output)

  '''
  -----------------------------------------------------
  Works for all testcases except #49
  Gives "Time Limit Exceeded" error but the code works!
  -----------------------------------------------------
  '''
