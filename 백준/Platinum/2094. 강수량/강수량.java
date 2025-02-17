import java.io.*;
import java.util.*;

public class Main {

	public static BufferedReader br;
	public static BufferedWriter bw;
	
    public static int n;
    public static int m;
    public static int base;
    public static int[] indexTree;
    public static int[] years;
    public static HashMap<Integer, Integer> map;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        base = 1;
        
        while (base < n) {
        	base <<= 1;
        }
        
        indexTree = new int[base * 2];
        years = new int[n+1];
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // 인덱스 트리 생성, 연도 연결 정보 기록
        for (int i = 1; i < (n+1); i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int year = Integer.parseInt(st.nextToken());
        	int rain = Integer.parseInt(st.nextToken());
        	
        	years[i] = year;
        	map.put(year, i);
        	
        	update(i, rain);
        }
        
        m = Integer.parseInt(br.readLine());
        
        // 사람들의 이야기 입력, 쿼리 진행
        for (int i = 0; i < m; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int yearY = Integer.parseInt(st.nextToken());
        	int yearX = Integer.parseInt(st.nextToken());
        	
        	// 1. Y와 X 정보 모두 없다면 항상 maybe 출력
        	if (!map.containsKey(yearY) && !map.containsKey(yearX)) {
        		bw.write("maybe\n");
        	}
        	// 2. Y의 정보만 있다면, Y+1부터 X-1 사이의 최댓값보다 Y가 클 경우 -> maybe
        	else if (map.containsKey(yearY) && !map.containsKey(yearX)) {
        		int left = map.get(yearY) + 1;
        		int right = binarySearch(yearX) - 1;
        		int maxRain = query(left, right);
        		
        		if (maxRain < indexTree[map.get(yearY) + base - 1]) {
        			bw.write("maybe\n");
        		} else {
        			bw.write("false\n");
        		}
        	}
        	// 3. X의 정보만 있다면, Y부터 X-1 사이의 최댓값보다 X가 클 경우 -> maybe
        	else if (!map.containsKey(yearY) && map.containsKey(yearX)) {
        		int left = binarySearch(yearY);
        		int right = map.get(yearX) - 1;
        		int maxRain = query(left, right);
        		
        		if (maxRain < indexTree[map.get(yearX) + base - 1]) {
        			bw.write("maybe\n");
        		} else {
        			bw.write("false\n");
        		}
        	}
        	// 4. X와 Y 정보 모두 있다면, Y+1부터 X-1 사이의 최댓값보다 X가 클 경우
        	// -> 연속 조건도 참인 경우: true
        	// -> 연속 조건은 거짓일 경우: maybe
        	else {
        		int left = map.get(yearY) + 1;
        		int right = map.get(yearX) - 1;
        		int maxRain = query(left, right);
        		
        		if (maxRain < indexTree[map.get(yearX) + base - 1] && indexTree[map.get(yearY) + base - 1] >= indexTree[map.get(yearX) + base - 1]) {
        			if ((right + 1) - (left - 1) == yearX - yearY) {
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
        br.close();
        bw.close();
    }
    
    public static void update(int idx, int value) throws IOException {
    	
    	idx = idx + base - 1;
    	
    	indexTree[idx] = value;
    	
    	while (idx > 1) {
    		idx /= 2;
    		indexTree[idx] = Math.max(indexTree[idx * 2], indexTree[idx * 2 + 1]);
    	}
    }
    
    static int query(int left, int right) throws IOException{
    	
        int result = 0;
        
        left += base - 1;
        right += base - 1;

        while(left <= right){
            if(left % 2 == 1){
                result = Math.max(result, indexTree[left]);
                left++;
            }

            if(right % 2 == 0){
                result = Math.max(result, indexTree[right]);
                right--;
            }

            left /= 2;
            right /= 2;
        }

        return result;
    }
    
    public static int binarySearch(int year) {
    	int start = 1;
    	int end = n;
    	
    	while (start < end) {
    		int mid = (start + end) / 2;
    		
    		int midYear = years[mid];
    		
    		if (midYear < year) {
    			start = mid + 1;
    		} else {
    			end = mid;
    		}
    	}
    	
    	return end;
    }
}