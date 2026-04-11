#include <bits/stdc++.h>

using namespace std;

int solution(vector<string> spell, vector<string> dic) {
    vector<string> result; 
    sort(spell.begin(), spell.end());
    
    do {
        string start = "";
        string temp = accumulate(spell.begin(), spell.end(), start);
        result.push_back(temp);
    } while (next_permutation(spell.begin(), spell.end()));
    
    for (auto d : dic) {
        if (find(result.begin(), result.end(), d) != result.end()) {
            return 1;
        }
    }
    
    return 2;
}