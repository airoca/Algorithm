import java.util.Arrays;

class Solution {
    public int solution(int[] array, int n) {
        
        int answer = 0;
        int minValue = 100;
        
        Arrays.sort(array);
        
        for (int cur : array) {
            if (minValue > Math.abs(cur - n)) {
                answer = cur;
                minValue = Math.abs(cur - n);
            }
        }
        
        return answer;
    }
}