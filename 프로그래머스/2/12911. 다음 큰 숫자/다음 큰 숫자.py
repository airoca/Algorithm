def solution(n):
    
    binary = format(n,"b")
    length = len(binary.replace("0",""))
    answer = n
    
    while True:
        answer += 1
        if len(format(answer,"b").replace("0","")) == length:
            break
    
    return answer