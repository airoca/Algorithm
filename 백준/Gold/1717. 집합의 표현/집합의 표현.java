import java.io.*;
import java.util.*;

public class Main {
    
	static BufferedReader br;
	static BufferedWriter bw;
	static StringTokenizer st;
	
	static int n, m;
	static int[] parent;
	
    public static void main(String[] args) throws Exception{
    	br = new BufferedReader(new InputStreamReader(System.in));
    	bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	st = new StringTokenizer(br.readLine());
    	n = Integer.parseInt(st.nextToken());
    	m = Integer.parseInt(st.nextToken());
    	
    	parent = new int[n+1];
    	for (int i = 0; i <= n; i++) {
    		parent[i] = i;
    	}
    	
    	int flag, a, b;
    	for (int i = 0; i < m; i++) {
    		st = new StringTokenizer(br.readLine());
    		flag = Integer.parseInt(st.nextToken());
        	if (flag == 0) {
        		a = Integer.parseInt(st.nextToken());
        		b = Integer.parseInt(st.nextToken());
        		union(a,b);
        	} else {
        		a = Integer.parseInt(st.nextToken());
        		b = Integer.parseInt(st.nextToken());
        		if (find(a) == find(b)) {
        			bw.write("YES\n");
        		} else {
        			bw.write("NO\n");
        		}
        	}
    	}
    	
    	bw.flush();
    	bw.close();
    	br.close();
    }
    
    static void union(int a, int b) {
    	int parentA = find(a);
    	int parentB = find(b);
    	
    	parent[parentB] = parentA;
    }
    
    static int find(int x) {
    	if (x == parent[x]) {
    		return x;
    	}
    	
    	return parent[x] = find(parent[x]);
    }
}