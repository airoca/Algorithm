#include <bits/stdc++.h>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = n * *max_element(times.begin(), times.end());
    long long left, right, mid, temp;
    
    left = 1;
    right = (long long)n * *max_element(times.begin(), times.end());
    
    while (left <= right) {
        mid = (left + right) / 2;
        temp = 0;
        
        for (auto t : times) {
            temp += (mid / t);
        }
        
        if (temp >= n) {
            answer = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return answer;
}