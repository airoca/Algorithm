#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;
int answer;

int dfs(int cur, int parent, int n) {
    int size = 1;
    
    for (auto nxt : graph[cur]) {
        if (nxt == parent) continue;
        int child_size = dfs(nxt, cur, n);
        int diff = abs(child_size - (n - child_size));
        answer = min(answer, diff);
        size += child_size;
    }
    
    return size;
}

int solution(int n, vector<vector<int>> wires) {
    answer = INT_MAX;
    graph.resize(n+1);
    
    for (auto v : wires) {
        int v1 = v[0];
        int v2 = v[1];
        graph[v1].push_back(v2);
        graph[v2].push_back(v1);
    }
    
    dfs(1, 0, n);
    
    return answer;
}
