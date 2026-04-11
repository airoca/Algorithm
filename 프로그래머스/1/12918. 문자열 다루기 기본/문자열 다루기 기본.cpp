#include <bits/stdc++.h>

using namespace std;

bool solution(string s) {
    bool answer = true;
    vector<char> n = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    
    if (s.size() != 4 && s.size() != 6) {
        return false;
    }
    
    for (auto c : s) {
        if (find(n.begin(), n.end(), c) == n.end()) {
            answer = false;
            break;
        }
    }
    
    return answer;
}