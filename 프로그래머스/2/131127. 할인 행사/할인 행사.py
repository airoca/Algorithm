def solution(want, number, discount):
    answer = 0
    d = {}
    for i in range(len(want)):
        d[want[i]] = number[i]
    
    for i in range(10):
        if (discount[i] in d):
            d[discount[i]] -= 1
    
    if validate(d):
        answer += 1
    
    left = 1
    right = 10
    
    while right < len(discount):
        if discount[right] in d:
            d[discount[right]] -= 1
        if discount[left-1] in d:
            d[discount[left-1]] += 1
        if validate(d):
            answer += 1
        right += 1
        left += 1
    return answer
    
def validate(d):
    for value in d.values():
        if value > 0:
            return False
    return True
        