#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;

    for (auto num : arr) {
        if (answer.size() == 0) {
            answer.push_back(num);
        } else {
            if (answer.back() != num) {
                answer.push_back(num);
            }
        }
    }

    return answer;
}