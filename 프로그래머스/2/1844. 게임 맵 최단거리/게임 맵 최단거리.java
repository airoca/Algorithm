import java.util.*;

class Solution {
    
    static class Location {
        int x;
        int y;
        int cost;
        
        public Location(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
    
    static int n, m;
    static boolean[][] visited;
    static final int[] dx = { 0, 0, -1, 1 };
    static final int[] dy = { 1, -1, 0, 0 };
    
    public int solution(int[][] maps) {
        
        n = maps.length;
        m = maps[0].length;
        
        visited = new boolean[n][m];
        
        int answer = 0;
        answer = bfs(maps);
        return answer;
    }
    
    static int bfs(int[][] graph) {
        Deque<Location> queue = new ArrayDeque<>();
        queue.add(new Location(0,0,1));
        visited[0][0] = true;
        
        while (!queue.isEmpty()) {
            
            Location cur = queue.poll();
            int x = cur.x;
            int y = cur.y;
            int cost = cur.cost;
            
            if (x == n-1 && y == m-1) {
                return cost;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                
                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.add(new Location(nx, ny, cost+1));
                }
            }
        }
        
        return -1;
    }
}