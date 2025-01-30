import java.util.Stack;

class Solution {
    public int solution(String s) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (String digit : s.split(" ")) {
            if (digit.equals("Z")) {
                stack.pop();
            }
            else {
                stack.push(Integer.parseInt(digit));
            }
        }
        
        for (int i : stack) {
            answer += i;
        }
        
        return answer;
    }
}