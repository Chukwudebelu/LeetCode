//!/bin/java
import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        // Create HashMap object to hold characters and frequencies
        HashMap<Character, Integer> dict_s = new HashMap<Character, Integer>();
        int count_s = 0;

        for (int i = 0; i < s.length(); i++) {
            if (dict_s.get(s.charAt(i)) == null) {
                dict_s.put(s.charAt(i), 0);
            } else {
                count_s++;
                dict_s.put(s.charAt(i), count_s);
            }
        }

        HashMap<Character, Integer> dict_t = new HashMap<Character, Integer>();
        int count_t = 0;

        for (int j = 0; j < t.length(); j++) {
            if (dict_t.get(t.charAt(j)) == null) {
                dict_t.put(t.charAt(j), 0);
            } else {
                count_t++;
                dict_t.put(t.charAt(j), count_t);
            }
        }

        return dict_t.equals(dict_s);
    }
}
