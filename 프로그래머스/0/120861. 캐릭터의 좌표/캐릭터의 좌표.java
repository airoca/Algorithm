class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        
        int[] answer = {0,0};
        
        for (String s : keyinput) {
            if (s.equals("left") && answer[0] > -board[0]/2)
                answer[0]--;
            else if (s.equals("right") && answer[0] < board[0]/2)
                answer[0]++;
            else if (s.equals("up") && answer[1] < board[1]/2)
                answer[1]++;
            else if (s.equals("down") && answer[1] > -board[1]/2)
                answer[1]--;
        }
        
        return answer;
    }
}