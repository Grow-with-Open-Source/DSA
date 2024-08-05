import java.util.HashMap;
import java.util.Map;

class Main {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> countS = new HashMap<>();
        Map<Character, Integer> countT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            countS.put(c1, countS.getOrDefault(c1, 0) + 1);
        }
    
        for (int i = 0; i < t.length(); i++) {
            char c2 = t.charAt(i);
            countT.put(c2, countT.getOrDefault(c2, 0) + 1);
        }
        
        for (char c : countS.keySet()) {
            if (!countT.containsKey(c) || !countT.get(c).equals(countS.get(c))) {
                return false;
            }
        }
        
        return true;
    }
}
