//!/bin/java
import java.lang.Math;

class Solution {
  public List<Integer> getRow(int rowIndex) {
    // Create a new array for each Binomial coefficient
    ArrayList<Integer> coeffs = new ArrayList<Integer>();
    
    for (int i = 0; i <= rowIndex; i++) {
      coeffs.add(combination(rowIndex, i));
    }
    return coeffs;
  }
    
  public static int combination(int n, int r) {
  // Compute nCr = n!/[r!(n-r)!]
    return (int) Math.round(factorial(n) /(factorial(r) * factorial(n-r)));
  }

  public static double factorial(int z) {
  // Computes z! = z x (z-1) x (z-2) x ... x 2 x 1
    double fac = 1;
    for (double i = 1; i <= z; i++)
      fac *= i;
    return fac;
  }
}
