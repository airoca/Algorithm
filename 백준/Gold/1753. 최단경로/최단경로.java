import java.io.*;
import java.util.*;

public class Main {
    
	static BufferedReader br;
	static BufferedWriter bw;
	static StringTokenizer st;
	
	static int n, m, root;
	static ArrayList<Node>[] adjList;
	static boolean[] visited;
	static int[] costs;
	
	static class Node implements Comparable<Node>{
	
		int index;
		int cost;
		
		public Node(int index, int cost) {
			this.index = index;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o) {
			return this.cost - o.cost;
		}
	}

    public static void main(String[] args) throws Exception {
    	
    	br = new BufferedReader(new InputStreamReader(System.in));
    	bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	
    	st = new StringTokenizer(br.readLine());
    	n = Integer.parseInt(st.nextToken());
    	m = Integer.parseInt(st.nextToken());
    	root = Integer.parseInt(br.readLine());
    	
    	adjList = new ArrayList[n+1];
    	visited = new boolean[n+1];
    	costs = new int[n+1];
    	for (int i = 1; i <= n; i++) {
    		adjList[i] = new ArrayList<>();
    		costs[i] = Integer.MAX_VALUE;
    	}
    	
    	int from, to, cost;
    	for (int i = 1; i <= m; i++) {
    		st = new StringTokenizer(br.readLine());
    		from = Integer.parseInt(st.nextToken());
    		to = Integer.parseInt(st.nextToken());
    		cost = Integer.parseInt(st.nextToken());
    		adjList[from].add(new Node(to, cost));
    	}
    	
    	dijkstra();
    	
    	for (int i = 1; i <= n; i++) {
    		if (costs[i] == Integer.MAX_VALUE) {
    			bw.write("INF\n");
    		} else {
    			bw.write(costs[i] + "\n");
    		}
    	}
    	
    	bw.flush();
    	br.close();
    	bw.close();
    }
    
    static void dijkstra() {
    	PriorityQueue<Node> queue = new PriorityQueue<>();
    	queue.add(new Node(root, 0));
    	costs[root] = 0;
    	
    	while (!queue.isEmpty()) {
    		Node cur = queue.poll();
    		
    		if (visited[cur.index]) {
    			continue;
    		}
    		
    		visited[cur.index] = true;
    		
    		for (Node next : adjList[cur.index]) {
    			if (costs[next.index] > cur.cost + next.cost) {
    				costs[next.index] = cur.cost + next.cost;
    				queue.add(new Node(next.index, costs[next.index]));
    			}
    		}	
    	}
    }
}