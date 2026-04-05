#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    int n = progresses.size();
    
    for (int i=0; i<n; i++) {
        int progress = progresses[i];
        int speed = speeds[i];
        q.push((100 - progress - 1) / speed + 1);
    }
    
    int day = q.front();
    q.pop();
    int temp = 1;
    
    while (q.size() > 0) {
        int cur_day = q.front();
        q.pop();
        if (day >= cur_day) {
            temp += 1;
        } else {
            answer.push_back(temp);
            day = cur_day;
            temp = 1;
        }
    }
    
    answer.push_back(temp);
    
    return answer;
}