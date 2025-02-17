import java.io.*;
import java.util.*;

public class Main {
    
	static BufferedReader br;
	static BufferedWriter bw;
	static StringTokenizer st;
	
	static int n, m, k, base;
	static long[] indexTree;
	
    public static void main(String[] args) throws Exception{
    	br = new BufferedReader(new InputStreamReader(System.in));
    	bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	st = new StringTokenizer(br.readLine());
    	n = Integer.parseInt(st.nextToken());
    	m = Integer.parseInt(st.nextToken());
    	k = Integer.parseInt(st.nextToken());
    	
    	base = 1;
    	while (base < n) {
    		base <<= 1;
    	}
    	
    	indexTree = new long[base * 2];
    	
    	for (int i = 1; i <= n; i++) {
    		long value = Long.parseLong(br.readLine());
    		update(i, value);
    	}
    	
    	for (int i = 0; i < (m+k); i++) {
    		st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	
        	// b번째 수를 c로 바꾼다.
        	if (a == 1) {
        		int b = Integer.parseInt(st.nextToken());
        		long c = Long.parseLong(st.nextToken());
            	update(b, c);
        	}
        	
        	// b번째 수부터 c번째 수까지 합을 출력한다.
        	if (a == 2) {
        		int b = Integer.parseInt(st.nextToken());
            	int c = Integer.parseInt(st.nextToken());
            	printSum(b, c);
        	}
    	}
    	
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static void update(int index, long value) {
    	index = index + base - 1;
    	indexTree[index] = value;
    	
    	while (index > 1) {
    		index /= 2;
    		indexTree[index] = indexTree[index*2] + indexTree[index*2 + 1];
    	}
    }
    
    static void printSum(int left, int right) throws IOException {
    	left = left + base - 1;
    	right = right + base - 1;
    	
    	long answer = 0;
    	
    	while (left <= right) {
    		
    		if (left % 2 != 0) {
    			answer += indexTree[left];
    			left++;
    		}
    		
    		if (right % 2 == 0) {
    			answer += indexTree[right];
    			right--;
    		}
    		
    		left = left/2;
    		right = right/2;
    	}
    	
    	bw.write(answer + "\n");
    }
}