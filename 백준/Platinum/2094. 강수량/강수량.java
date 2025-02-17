import java.io.*;
import java.util.*;

public class Main {
    
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    
    static int n, m, base;
    static int[] indexTree;
    static HashMap<Integer, Integer> map;
    static int[] years;

    public static void main(String[] args) throws IOException {
        
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        map = new HashMap<Integer, Integer>();
        
        base = 1;
        while (base < n) {
        	base <<= 1;
        }
        
        indexTree = new int[base * 2];
        years = new int[n+1];
        
        for (int i = 1; i <= n; i++) {
        	st = new StringTokenizer(br.readLine());
        	int y = Integer.parseInt(st.nextToken());
        	int r = Integer.parseInt(st.nextToken());
        	map.put(y, i);
        	update(i,r);
        	years[i] = y;
        }
        
        m = Integer.parseInt(br.readLine());
        
        int y, x, left, right, maxValue;
        for (int i = 0; i < m; i++) {
        	st = new StringTokenizer(br.readLine());
        	y = Integer.parseInt(st.nextToken());
        	x = Integer.parseInt(st.nextToken());
        	
        	// y의 값과 x의 값 모두 존재하지 않을 때
        	// 무조건 maybe를 출력
        	if (!map.containsKey(y) && !map.containsKey(x)) {
        		bw.write("maybe\n");
        	}
        	
        	// y의 값만 존재할 때
        	// (y + 1) ~ (x 직전 값) 의 최대값보다 y의 값이 더 크다면 -> maybe
        	else if (map.containsKey(y) && !map.containsKey(x)) {
        		left = map.get(y) + 1;
        		right = binarySearch(x) - 1;
        		maxValue = query(left, right);
        		
        		if (maxValue < indexTree[map.get(y) + base - 1]) {
        			bw.write("maybe\n");
        		} else {
        			bw.write("false\n");
        		}
        	}
        	
        	// x의 값만 존재할 때
        	// (y 직후 값) ~ (x - 1) 의 최대값보다 x의 값이 더 크다면 -> maybe
        	else if (!map.containsKey(y) && map.containsKey(x)) {
        		left = binarySearch(y);
        		right = map.get(x) - 1;
        		maxValue = query(left, right);
        		
        		if (maxValue < indexTree[map.get(x) + base - 1]) {
        			bw.write("maybe\n");
        		} else {
        			bw.write("false\n");
        		}
        	}
        	
        	// y, x 모두 존재할 때
        	// y >= x를 만족하고, (y + 1) ~ (x - 1) 의 최대값보다 x가 더 크다면 -> maybe
        	// 중간에 빈 값도 없다면 -> true
        	else {
        		left = map.get(y) + 1;
        		right = map.get(x) - 1;
        		maxValue = query(left, right);
        		
        		if (indexTree[map.get(y) + base - 1] >= indexTree[map.get(x) + base - 1] && maxValue < indexTree[map.get(x) + base - 1]) {
        			if (x - y == map.get(x) - map.get(y)) {
        				bw.write("true\n");
        			} else {
        				bw.write("maybe\n");
        			}
        		} else {
        			bw.write("false\n");
        		}
        	}
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
    
    static void update(int index, int value) {
    	index = index + base - 1;
    	indexTree[index] = value;
    	
    	while (index > 1) {
    		index /= 2;
    		indexTree[index] = Math.max(indexTree[index * 2], indexTree[index * 2 + 1]);
    	}
    }
    
    static int query(int left, int right) {
    	
    	left = left + base - 1;
    	right = right + base - 1;
    	
    	int maxValue = 0;
    	
    	while (left <= right) {
    		if (left % 2 != 0) {
    			maxValue = Math.max(maxValue, indexTree[left]);
    			left++;
    		}
    		
    		if (right % 2 == 0) {
    			maxValue = Math.max(maxValue, indexTree[right]);
    			right--;
    		}
    		
    		left /= 2;
    		right /= 2;
    	}
    	
    	return maxValue;
    }
    
    static int binarySearch(int year) {
    	
    	int start = 1;
    	int end = n;
    	
    	while (start < end) {
    		int mid = (start + end) / 2;
    		
    		if (years[mid] < year) {
    			start = mid + 1;
    		} else {
    			end = mid;
    		}
    	}
    	
    	return end;
    }
}