class Solution {
    public String addBinary(String a, String b) {
        int m = a.length(); int n = b.length();
        
        // If a or b is empty
        if (m == 0)
            return b;
        if (n == 0)
            return a;
        // String to hold sum
        String s = "";
        int carry = 0;
        
        // Initialize indexes
        int i = m-1;
        int j = n-1;
        
        // Get char arrays
        char[] a_c = a.toCharArray();
        char[] b_c = b.toCharArray();
        
        while (i >= 0 || j >= 0 || carry > 0) {
            if (i >= 0) {
                carry += Integer.parseInt("" + a_c[i]);
                i -= 1;
            }
            if (j >= 0) {
                carry += Integer.parseInt("" + b_c[j]);
                j -= 1;
            }
            s = "" + carry%2 + "" + s;
            carry /= 2;
        }
        return s;
    }
}
