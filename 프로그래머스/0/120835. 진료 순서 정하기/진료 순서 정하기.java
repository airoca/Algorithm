import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        int[][] indexEmergency = new int [emergency.length][2];
        
        for (int i = 0; i < emergency.length; i++){
            indexEmergency[i][0] = i;
            indexEmergency[i][1] = emergency[i];
        }
        
        Arrays.sort(indexEmergency, (a,b) -> Integer.compare(b[1], a[1]));
        
        int[] answer = new int[emergency.length];
        
        for (int i = 0; i < emergency.length; i++){
            int originIndex = indexEmergency[i][0];
            answer[originIndex] = i + 1;
        }
        
        return answer;
    }
}