#include <bits/stdc++.h>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    int left, right, mid;
    left = 0;
    right = distance;
    
    sort(rocks.begin(), rocks.end());
    
    while (left <= right) {
        mid = (left + right) / 2;
        
        int prev = 0;
        int removed = 0;
        
        for (auto r : rocks) {
            if (r - prev < mid) {
                removed++;
            } else {
                prev = r;
            }
        }
        
        if (distance - prev < mid) {
            removed++;
        }
        
        if (removed > n) {
            right = mid - 1;
        } else {
            answer = mid;
            left = mid + 1;
        }
    }
    
    return answer;
}