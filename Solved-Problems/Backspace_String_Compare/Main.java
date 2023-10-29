
//Problem Name: 844.Backspace String Compare

//Approach: Using Stacks

//Difficulty: Easy

//Link: https://leetcode.com/problems/backspace-string-compare/

import java.util.Stack;

class Main {

    public static boolean backspaceCompare(String s, String t) {
        Stack<Character> s1 = new Stack<>();
        Stack<Character> s2 = new Stack<>();

        for (char ch : s.toCharArray()) {
            if (ch == '#') {
                if (!s1.isEmpty()) {
                    s1.pop();
                }
                continue;
            }
            s1.push(ch);
        }

        for (char ch : t.toCharArray()) {
            if (ch == '#') {
                if (!s2.isEmpty()) {
                    s2.pop();
                }
                continue;
            }
            s2.push(ch);
        }

        StringBuilder res1 = new StringBuilder();
        StringBuilder res2 = new StringBuilder();

        while (!s1.isEmpty()) {
            res1.append(s1.pop());
        }

        while (!s2.isEmpty()) {
            res2.append(s2.pop());
        }

        return res1.toString().equals(res2.toString());
    }

    public static void main(String[] args) {
        String s = "ab#c";
        String t = "ad#c";
        System.out.println(backspaceCompare(s, t));
    }
}



// LEETCODE SOLUTION

// import java.util.*;
// class Solution {
//     public boolean backspaceCompare(String s, String t) {
//         Stack<Character> s1 = new Stack<Character>();
//         Stack<Character> s2 = new Stack<Character>();
        
//         for(char ch : s.toCharArray()){
//             if(ch == '#'){
//                 if(!s1.isEmpty())
//                     s1.pop();
//                 continue;
//             }
//             s1.push(ch);
//         }
        
//         for(char ch : t.toCharArray()){
//             if(ch == '#'){
//                 if(!s2.isEmpty())
//                     s2.pop();
//                 continue;
//             }
//             s2.push(ch);
//         }
        
//         String res1 = "";
//         String res2 = "";
        
//         while(!s1.isEmpty())
//             res1 += s1.pop();
        
//         while(!s2.isEmpty())
//             res2 += s2.pop();
        
//         return res1.equals(res2);
//     }
// }

