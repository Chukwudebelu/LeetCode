//!/bin/java

class Solution {
  public List<Integer> getRow(int rowIndex) {
    List<List<Integer>> arr = new ArrayList<List<Integer>>();
    ArrayList<Integer> s0 = new ArrayList<>();
    s0.add(1);
    arr.add(s0);

    ArrayList<Integer> s1 = new ArrayList<>();
    s1.add(1);
    s1.add(1);
    arr.add(s1);

    for (int i = 2; i < rowIndex+1; i++) {
      ArrayList<Integer> si = new ArrayList<Integer>();
      si.add(1); // [1, ...]
      int len = arr.get(i-1).size();
      for (int j = 1; j < len; j++) {
        int num = arr.get(i-1).get(j-1) + arr.get(i-1).get(j);
        si.add(num);
      }
      si.add(1); // [..., 1]
      arr.add(si);
    }
    return arr.get(rowIndex);
  }
}
