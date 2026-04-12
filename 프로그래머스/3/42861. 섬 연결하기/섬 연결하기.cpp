#include <bits/stdc++.h>

using namespace std;

vector<int> parent;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

bool unite(int x, int y) {
    int px = find(x);
    int py = find(y);
    
    if (px == py) {
        return false;
    } else {
        parent[py] = px;
        return true;
    }
}

bool cmp(vector<int> v1, vector<int> v2) {
    return v1[2] < v2[2];
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    for (int i = 0; i < n; i++) {
        parent.push_back(i);
    }
    
    sort(costs.begin(), costs.end(), cmp);
    
    for (auto c : costs) {
        int v1 = c[0];
        int v2 = c[1];
        int dist = c[2];
        
        if (unite(v1, v2)) {
            answer += dist;
        }
    }
    
    return answer;
}