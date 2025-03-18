def solution(k, tangerine):
    
    count = [0] * 10000001
    
    for fruit in tangerine:
        count[fruit] += 1
    
    count = [c for c in count if c != 0]
    count.sort(reverse = True)
    
    answer = 1
    
    for c in count:
        if c >= k:
            return answer
        else:
            k -= c
            answer += 1
            
    return answer