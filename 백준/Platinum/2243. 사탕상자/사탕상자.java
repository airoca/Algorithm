import java.util.*;
import java.io.*;

public class Main {
	
	static BufferedReader br;
	static BufferedWriter bw;
	static int base;
	static int[] indexTree;
	
	public static void main(String[] args) throws IOException {
		
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		base = 1;
		
		while (base < 1000000) {
			base <<= 1;
		}
		
		indexTree = new int[base * 2];
		
		StringTokenizer st;
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			if (a == 1) {
				int b = Integer.parseInt(st.nextToken());
				bw.write(pick(b) + "\n");
			} else {
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				update(b,c);
			}
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
	
	private static void update(int index, int value) {
		index = index + base - 1;
		indexTree[index] += value;
		
		while (index > 1) {
			index /= 2;
			indexTree[index] = indexTree[index*2] + indexTree[index*2+1];
		}
	}
	
	private static int pick(int rank) {
		int index = 1;
		
		while (index < base) {
			if (indexTree[index * 2] >= rank) {
				index = index * 2;
			} else {
				rank -= indexTree[index * 2];
				index = index * 2 + 1;
			}
		}
		
		update(index - base + 1,-1);
		
		return index - base + 1;
	}
}