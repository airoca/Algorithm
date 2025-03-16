import java.io.*;
import java.util.*;

import javax.management.Query;

public class Main {
    
    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;
    
    static class Edge implements Comparable<Edge>{
    	int start;
    	int end;
    	int weight;
    	
    	public Edge(int start, int end, int weight) {
    		this.start = start;
    		this.end = end;
    		this.weight = weight;
    	}
    	
    	@Override
    	public int compareTo(Edge o) {
    		return weight - o.weight;
    	}
    }
    
    static int n, m, result;
    static ArrayList<Edge> edges;
    static int[] parent;
    
    public static void main(String[] args) throws IOException {
        
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        edges = new ArrayList<Edge>();
        parent = new int[n+1];
        
        for (int i = 1; i <= n; i++) {
        	parent[i] = i;
        }
        
        for (int i = 0; i < m; i++) {
        	st = new StringTokenizer(br.readLine());
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	int c = Integer.parseInt(st.nextToken());
        	edges.add(new Edge(a,b,c));
        }
        
        Collections.sort(edges);
        
        result = 0;
        
        for (Edge edge : edges) {
        	int start = edge.start;
        	int end = edge.end;
        	int weight = edge.weight;
        	
        	if (find(start) != find(end)) {
        		result += weight;
        		union(start, end);
        	}
        }
        
        bw.append(result + "");
        
        bw.flush();
        bw.close();
        br.close();
    }
    
    static int find(int x) {
    	if (x == parent[x]) {
    		return x;
    	}
    	return parent[x] = find(parent[x]);
    }
    
    static void union(int a, int b) {
    	int parentA = find(a);
    	int parentB = find(b);
    	
    	if (parentA != parentB) {
    		parent[parentB] = parentA;
    	}
    }
}