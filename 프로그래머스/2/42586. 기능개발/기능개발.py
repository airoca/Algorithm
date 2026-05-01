from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
        day = (100 - progresses[i] + speeds[i] - 1) // speeds[i]
        queue.append(day)
    
    cur_day = queue.popleft()
    count = 1
    
    while queue:
        day = queue.popleft()
        if day <= cur_day:
            count += 1
        else:
            answer.append(count)
            cur_day = day
            count = 1
    
    answer.append(count)
    
    return answer