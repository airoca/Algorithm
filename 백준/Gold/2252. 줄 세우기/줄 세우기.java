import java.io.*;
import java.util.*;

public class Main {

	public static BufferedReader br;
	public static BufferedWriter bw;
	static StringTokenizer st;
	
	static ArrayList<ArrayList<Integer>> graph;
	static int[] edgeCount;

	public static void main(String[] args) throws IOException {
		
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i <= n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }
		
		edgeCount = new int[n+1];
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			edgeCount[b]++;
		}
		
		Deque<Integer> queue = new ArrayDeque<>();
		
		for (int i = 1; i <= n; i++) {
            if (edgeCount[i] == 0) {
                queue.add(i);
            }
        }
		
		while (!queue.isEmpty()) {
			int student = queue.poll();
			bw.write(student + " ");
			
			List<Integer> list = graph.get(student);
			for (int i = 0; i < list.size(); i++) {
				int temp = list.get(i);
				if (--edgeCount[temp] == 0) {
					queue.add(temp);
				}
			}
		}
		
		bw.flush();
		br.close();
		bw.close();
	}
	
}