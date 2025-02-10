import java.io.*;
import java.util.*;

public class Main {

	public static BufferedReader br;
	public static BufferedWriter bw;
	
	static int[][] dp;
	static StringBuilder sb;
	static int MAX_VALUE = 1_000_000_000;

	public static void main(String[] args) throws IOException {
		
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
		sb = new StringBuilder();
		dp = new int[n+1][m+1];
		
		if (combination(n,m) < k) {
			System.out.println(-1);
		} else {
			find(n,m,k);
			System.out.println(sb);
		}
		
		br.close();
		bw.close();
	}
	
	private static int combination(int n, int m) {
		if (n == 0 || m == 0) {
			return 1;
		} else if (dp[n][m] != 0) {
			return dp[n][m];
		} else {
			dp[n][m] = Math.min(combination(n,m-1) + combination(n-1,m), MAX_VALUE);
		}
		
		return dp[n][m];
	}
	
	private static void find(int n, int m, int k) {
		if (n == 0) {
			for (int i = 0; i < m; i++) {
				sb.append("z");
			}
			return;
		} else if (m == 0) {
			for (int i = 0; i < n; i++) {
				sb.append("a");
			}
			return;
		}
		
		int cur = combination(n-1,m);
		
		if (k > cur) {
			sb.append("z");
			find(n, m-1, k-cur);
		} else {
			sb.append("a");
			find(n-1, m, k);
		}
	}
}