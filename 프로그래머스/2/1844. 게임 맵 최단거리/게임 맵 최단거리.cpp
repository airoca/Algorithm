#include<vector>
#include<queue>
using namespace std;

int solution(vector<vector<int> > maps)
{
    int n = maps.size();
    int m = maps[0].size();
    queue<pair<int,int>> q;
    int dx[] = {1,-1,0,0};
    int dy[] = {0,0,1,-1};
    
    q.push({0,0});
    
    while (q.size() > 0) {
        auto [x,y] = q.front();
        q.pop();
        
        if (x == n-1 && y == m-1) {
            return maps[x][y];
        }
        
        for (int i=0; i<4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (maps[nx][ny] != 1) continue;
            maps[nx][ny] = maps[x][y] + 1;
            q.push({nx,ny});
        }
    }
    
    return -1;
}