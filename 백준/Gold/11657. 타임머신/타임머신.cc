#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() 
{
  int n, m;
  ll INF = 1e18;
  cin >> n >> m;
  
  vector<vector<pair<int, int>>> adj(n+1);
  vector<ll> dist(n+1, INF);
  dist[1] = 0;
  
  for (int i = 0; i < m; i++) {
     int x, y, d;
     cin >> x >> y >> d;
     adj[x].push_back({y, d});
  }
  
  for (int i = 0; i < n-1; i++) {
    for (int cur = 1; cur < n+1; cur++) {
      for (auto a : adj[cur]) {
        int nxt = a.first;
        int cur_dist = a.second;
        if (dist[cur] != INF) {
          dist[nxt] = min(dist[nxt], dist[cur] + cur_dist);
        }
      }
    }
  }
  
  bool iscycle = false;
  
  for (int cur = 1; cur < n+1; cur++) {
    for (auto a : adj[cur]) {
      int nxt = a.first;
      int cur_dist = a.second;
      if (dist[cur] != INF && dist[nxt] > dist[cur] + cur_dist) {
        iscycle = true;
      }
    }
  }
  
  if (iscycle) {
    cout << -1;
  } else {
    for (int i = 2; i < n+1; i++) {
      if (dist[i] == INF) {
        cout << -1 << "\n";
      } else {
        cout << dist[i] << "\n"; 
      }
    }
  }
}