def solution(clothes):
    
    d = {}
    
    for cloth in clothes:
        if cloth[1] in d:
            d[cloth[1]] += 1
        else:
            d[cloth[1]] = 1
    
    answer = 1
    
    for i in d.values():
        answer *= (i+1)
    
    return answer-1