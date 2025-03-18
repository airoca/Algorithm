def solution(n):
    answer = 0
    
    lst = [0] * (n+1)
    
    for i in range(1,n+1):
        lst[i] = lst[i-1] + i
    
    left = 0
    right = 0
    
    result = []
    
    while right <= n:
        if lst[right] - lst[left] == n:
            answer += 1
            right += 1
        elif lst[right] - lst[left] < n:
            right += 1
        else:
            left += 1
    
    return answer