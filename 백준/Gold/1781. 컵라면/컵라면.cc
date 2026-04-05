#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
    vector<pair<int,int>> v;
    priority_queue<int, vector<int>, greater<int>> pq;
    int n;
    cin >> n;
    
    for (int i=0; i<n; i++) {
        int x, y;
        cin >> x >> y;
        v.push_back({x,y});
    }

    sort(v.begin(), v.end());

    for (auto [d,r] : v) {
        pq.push(r);
        while (pq.size() > d) {
            pq.pop();
        }
    }

    int answer = 0;

    while (!pq.empty()) {
        answer += pq.top();
        pq.pop();
    }

    cout << answer;
}