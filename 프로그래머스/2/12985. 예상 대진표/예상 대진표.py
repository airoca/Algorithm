def solution(n,a,b):
    base = n*2 + 1
    
    a += (n-1)
    b += (n-1)
    
    answer = 0
    
    while a != b:
        a //= 2
        b //= 2
        answer += 1

    return answer