import java.util.*;
import java.io.*;

public class Main {

    static BufferedReader br;
    static BufferedWriter bw;
    static StringTokenizer st;

    static int[] parent;
    static int[] weight;
    static int n, m;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            if (n == 0) {
                break;
            }

            parent = new int[n + 1];
            weight = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                parent[i] = i;
                weight[i] = 0;
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                String flag = st.nextToken();
                if (flag.equals("!")) {
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());
                    int w = Integer.parseInt(st.nextToken());
                    union(a, b, w);
                } else {
                    int a = Integer.parseInt(st.nextToken());
                    int b = Integer.parseInt(st.nextToken());
                    if (find(a) == find(b)) {
                        bw.write((weight[b] - weight[a]) + "\n");
                    } else {
                        bw.write("UNKNOWN\n");
                    }
                }
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }

    private static int find(int n) {
        if (n == parent[n]) {
            return n;
        }
        int root = find(parent[n]);
        weight[n] += weight[parent[n]];
        return parent[n] = root;
    }

    private static void union(int a, int b, int w) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) {
            return;
        }

        parent[rootB] = rootA;
        weight[rootB] = weight[a] - weight[b] + w;
    }
}