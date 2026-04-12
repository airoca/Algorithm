#include <bits/stdc++.h>

using namespace std;

int main() 
{
  int n, m;
  cin >> n >> m;
  vector<vector<int>> graph(n+1);
  vector<int> indegree(n+1, 0);
  deque<int> queue;
  
  for (int i = 0; i < m; i++) {
    int s1, s2;
    cin >> s1 >> s2;
    graph[s1].push_back(s2);
    indegree[s2]++;
  }
  
  for (int i = 1; i < n+1; i++) {
    if (indegree[i] == 0) {
      queue.push_back(i);
    }
  }
  
  vector<int> answer;
  
  while (!queue.empty()) {
    int cur = queue.front();
    queue.pop_front();
    
    answer.push_back(cur);
    
    for (auto nxt : graph[cur]) {
      indegree[nxt]--;
      if (indegree[nxt] == 0) {
        queue.push_back(nxt);
      }
    }
  }
  
  for (auto a : answer) {
    cout << a << " ";
  }
}