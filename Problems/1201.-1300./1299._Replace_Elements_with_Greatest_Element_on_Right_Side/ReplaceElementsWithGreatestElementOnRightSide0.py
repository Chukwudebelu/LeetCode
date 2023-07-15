class Solution:
  def replaceElements(self, arr: List[int]) -> List[int]:
    n = len(arr)
    if (n == 1): return [-1]
        
    # Replace the last element with -1
    temp = arr[n-1]; arr[n-1] = -1
    
    # Replace the 2nd last element with the last one
    max_value = max(temp, arr[n-2])
    arr[n-2] = temp
    
    # Continue with loop
    for i in range(n-3,-1,-1):
        temp = arr[i]
        arr[i] = max_value
        max_value = max(temp, max_value)
    return arr
