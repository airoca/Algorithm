import java.util.Arrays;

class Solution {
    public int solution(int[][] dots) {
        
         Arrays.sort(dots, (a, b) -> Integer.compare(a[0], b[0]));
        
        int answer = Math.abs((dots[0][1] - dots[1][1]) * (dots[1][0] - dots[2][0]));
        
        return answer;
    }
}