class Solution {
    public int solution(int[] numbers, int k) {
        int answer = 0;
        
        k = (k-1) * 2;
        int index = k % numbers.length; 
        answer = numbers[index];
        
        return answer;
    }
}