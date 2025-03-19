from collections import deque

def solution(progresses, speeds):
    
    queue = deque()
    answer = []
    
    for i in range(len(progresses)):
        queue.append((100 - progresses[i] - 1) // speeds[i] + 1)
    
    cur_day = queue.popleft()
    count = 1
    
    while queue:
        days = queue.popleft()
        if cur_day < days:
            cur_day = days
            answer.append(count)
            count = 1
        else:
            count += 1
    
    answer.append(count)
    
    return answer