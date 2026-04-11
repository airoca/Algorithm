#include<bits/stdc++.h>
using namespace std;

int solution(vector<vector<int> > maps)
{
    
    int n = maps.size();
    int m = maps[0].size();
    
    int dx[] = {1,-1,0,0};
    int dy[] = {0,0,1,-1};
    
    deque<vector<int>> queue;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    visited[0][0] = true;
    queue.push_back({0, 0, 1});
    
    while (!queue.empty()) {
        auto cur = queue.front();
        queue.pop_front();
        
        int x = cur[0];
        int y = cur[1];
        int cost = cur[2];
        
        if (x == n-1 && y == m-1) {
            return cost;
        }
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            
            if (!visited[nx][ny] && maps[nx][ny] != 0) {
                visited[nx][ny] = true;
                queue.push_back({nx, ny, cost + 1});
            }
        }
    }
    
    return -1;
}