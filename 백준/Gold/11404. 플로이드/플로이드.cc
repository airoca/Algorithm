#include <iostream>
#include <vector>
using namespace std;

int main() 
{
  int n, m;
  cin >> n >> m;
  int INF = 1e9;
  vector<vector<int>> dist(n+1, vector<int>(n+1, INF));
  
  for (int i = 1; i < n+1; i++) {
    dist[i][i] = 0;
  }
    
  for (int i = 0; i < m; i++) {
    int x, y, d;
    cin >> x >> y >> d;
    if (dist[x][y] > d) {
      dist[x][y] = d; 
    }
  }
  
  for (int k = 1; k < n+1; k++) {
    for (int i = 1; i < n+1; i++) {
      for (int j = 1; j < n+1; j++) {
        if (dist[i][k] != INF && dist[k][j] != INF) {
          dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
  }
  
  for (int i = 1; i < n+1; i++) {
    for (int j = 1; j < n+1; j++) {
      if (dist[i][j] == INF) {
        cout << 0 << " ";
      } else {
        cout << dist[i][j] << " "; 
      }
    }
    cout << "\n";
  }
}