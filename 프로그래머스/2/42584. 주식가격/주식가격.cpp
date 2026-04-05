#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    deque<int> q;
    
    for (auto x : prices) {
        q.push_back(x);
    }
    
    while (q.size() > 0) {
        int cur = q.front();
        q.pop_front();
        int temp = 0;
        for (auto nxt : q) {
            temp += 1;
            if (cur > nxt) break;
        }
        answer.push_back(temp);
    }
    
    return answer;
}