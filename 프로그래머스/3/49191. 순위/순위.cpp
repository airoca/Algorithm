#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<bool>> win(n+1, vector<bool>(n+1));
    
    for (auto r : results) {
       win[r[0]][r[1]] = true;
    }
    
    for (int k = 0; k < n+1; k++) {
        for (int i = 0; i < n+1; i++) {
            for (int j = 0; j < n+1; j++) {
                if (win[i][k] && win[k][j]) {
                    win[i][j] = true;
                }
            }        
        }
    }
    
    for (int i = 0; i < n+1; i++) {
        int cnt = 0;
        for (int j = 0; j < n+1; j++) {
            if (win[i][j] || win[j][i]) {
                cnt++;
            }
        }
        if (cnt == n-1) {
            answer++;
        }
    }
    
    return answer;
}