#include <string>
#include <vector>
#include <deque>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    const int INF = 1e9;
    int answer = 0;
    vector<vector<int>> adj(n+1);
    vector<int> cost(n+1, INF);
    cost[1] = 0;
    
    for (auto e : edge) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    
    deque<int> queue;
    queue.push_back(1);
    
    while (!queue.empty()) {
        int cur = queue.front();
        queue.pop_front();
        for (auto nxt : adj[cur]) {
            if (cost[nxt] == INF) {
                cost[nxt] = cost[cur] + 1;
                queue.push_back(nxt);
            }
        }
    }
    
    for (int i = 0; i < n+1; i++) {
        if (cost[i] == INF) {
            cost[i] = 0;
        }
    }
    
    int max = *max_element(cost.begin(), cost.end());
    answer = count(cost.begin(), cost.end(), max);
    
    return answer;
}