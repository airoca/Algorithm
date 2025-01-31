import java.util.Arrays;

class Solution {
    public long solution(String numbers) {
        String answer = "";
        String temp = "";
        String[] arr = {"zero","one","two","three","four","five",
                        "six","seven","eight","nine"};
        
        for (String s : numbers.split("")) {
            temp += s;
            if ((Arrays.asList(arr).contains(temp))) {
                answer += String.valueOf(Arrays.asList(arr).indexOf(temp));
                temp = "";
            }
        }
        
        long longAnswer = Long.parseLong(answer);
        
        return longAnswer;
    }
}