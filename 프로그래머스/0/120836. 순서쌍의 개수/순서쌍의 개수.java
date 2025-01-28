class Solution {
    public int solution(int n) {
        
        int answer = 0;
        int same = 0;
        
        for (int i = 1; i <= n; i++) {
            if (n%i == 0) {
                answer++;
                if (n/i == i){
                    same++;
                }
            }
        }
        
        answer -= same/2;
        
        return answer;
    }
}