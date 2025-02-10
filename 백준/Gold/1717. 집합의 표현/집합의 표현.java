import java.io.*;
import java.util.*;

public class Main {

	public static BufferedReader br;
	public static BufferedWriter bw;
	
	static int[] parent;

	public static void main(String[] args) throws IOException {
		
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		parent = new int[n+1];
		
		for (int i = 0; i <= n; i++) {
			parent[i] = i;
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int flag = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (flag == 0) {
				union(a, b);
			} else {
				if (find(a) == find(b)) {
					bw.write("YES\n");
				} else {
					bw.write("NO\n");
				}
			}
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
	
	public static void union(int a, int b) {
		int a_parent = find(a);
		int b_parent = find(b);
		
		if (a_parent < b_parent) {
			parent[b_parent] = a_parent;
		} else if (b_parent < a_parent){
			parent[a_parent] = b_parent;
		}
	}
	
	public static int find(int n) {
		if (parent[n] == n) {
			return n;
		} else {
			return parent[n] = find(parent[n]);
		}
	}
}