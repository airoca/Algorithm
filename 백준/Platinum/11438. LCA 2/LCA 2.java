import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

// 백준 11437 G3 : LOG = 16
// 백준 11438 P5 : LOG = 17
public class Main {
    // 2^15 = 32768
    // 2^16 = 65536
    // 2^17 = 131072
    // 최대 노드(N) 수 보다 큰 가장 작은 2^n 값을 선택하면 된다.
    // c.f. 2^15 < N=50000 < 2^16
    // c.f. 2^16 < N=100000 < 2^17
    static final int LOG = 17;
    
    static int N, M;
    static boolean[] visited;
    static ArrayList<Integer>[] adjList;
    static int[] depth;
    static int[][] parent;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        N = Integer.parseInt(br.readLine());
        visited = new boolean[N+1];
        depth = new int[N+1];
        parent = new int[LOG+1][N+1];

        // 0. input -> adjacent list
        adjList = new ArrayList[N+1];
        for(int i=1; i<=N; i++){
            adjList[i] = new ArrayList<>();
        }

        StringTokenizer st;
        int n1, n2;
        for(int n=0; n<N-1; n++){
            st = new StringTokenizer(br.readLine());
            n1 = Integer.parseInt(st.nextToken());
            n2 = Integer.parseInt(st.nextToken());
            
            // 양방향 간선으로 넣어준다(방향이 없는, 이어진)
            adjList[n1].add(n2);
            adjList[n2].add(n1);
        }

        // 1. bfs -> update parent[0][V] for all V
        bfs(1);

        // 2. findAncestors -> update parent[k][V]
        // parent[k][V] = parent[k-1][parent[k-1][V]]
        findAncestors();

        // 3. find lca
        M = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        int a, b;
        for(int m=0; m<M; m++){
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            sb.append(lca(a, b));
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();

    }

    static void bfs(int root){
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        // root: 1번 노드로 정함
        queue.add(root);
        depth[root] = 0;
        visited[root] = true;

        while(!queue.isEmpty()) {
            int currentNode = queue.poll();

            for (int nextNode : adjList[currentNode]) {
                if(!visited[nextNode]){
                    visited[nextNode] = true;

                    parent[0][nextNode] = currentNode;
                    depth[nextNode] = depth[currentNode] + 1;
                    queue.add(nextNode);
                }
            }
        }
    }

    static void findAncestors(){
        for(int k=1; k<=LOG; k++){
            for(int v=1; v<=N; v++){
                parent[k][v] = parent[k-1][parent[k-1][v]];
            }
        }
    }

    static int lca(int a, int b){
        // 0. 항상 b가 a보다 depth가 큰 노드(root로부터 먼)가 되도록 swap
        if(depth[a] > depth[b]){
            int temp = b;
            b = a;
            a = temp;
        }

        // 1. a, b의 depth 맞추기(0.에 의해 항상 b를 끌어올리게 된다)
        for(int k=LOG; k>=0; k--){
            // (1 << k) : 2^k
            // IF [(depth 차이) >= 2^16 ... 2^0] -> b 끌어올림
            // for loop의 마지막 수행 시 (depth 차이 = 1) > b = parent[0][b] 로 1 depth 끌어올려지므로 a, b의 depth가 동일해진다
            if(depth[b]-depth[a] >= (1 << k)){
                b = parent[k][b];
            }
        }

        // 2. 1.에서 depth를 맞추었는데 a와 b가 같다면 lca를 찾은 것
        if(a == b){
            return a;
        }

        // 3. a와 b를 같이 끌어올리면서 처음으로 조상이 같지 않은 지점(parent[0][a] != parent[0][b]) 까지 이동
        // a와 b의 조상이 같으면 k--
        // a와 b의 조상이 같지 않으면 a와 b를 2^k 만큼 끌어올림
        for(int k=LOG; k>=0; k--){
            if(parent[k][a] != parent[k][b]){
                a = parent[k][a];
                b = parent[k][b];
            }
        }

        // 4. 3.이 2^0=1 에서 끝났으므로 a, b의 바로 위 조상이 lca가 된다
        return parent[0][a];
    }
}