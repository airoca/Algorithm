class Solution {
    public String[] solution(String my_str, int n) {
        int length = my_str.length() % n == 0 ?
            my_str.length()/n : my_str.length()/n + 1;
        
        String[] answer = new String[length];
        
        int index = 0;
        
        for (int i = 0; i<my_str.length(); i+=n) {
            answer[index] = my_str.substring(i,Math.min(i + n, my_str.length()));
            index++;
        }
        
        return answer;
    }
}