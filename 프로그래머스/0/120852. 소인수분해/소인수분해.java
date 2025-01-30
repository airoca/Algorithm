import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 2; i<=n; i++) {
            if (n%i == 0) {
                answer.add(i);
                while (n%i == 0)
                    n /= i;
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}