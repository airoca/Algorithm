from collections import deque

def solution(priorities, location):
    
    queue = deque()
    answer = 1
    
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))
    
    while queue:
        index, value = queue.popleft()
        maxValue = max(priorities)
        if (value == maxValue):
            priorities.remove(maxValue)
            if index == location:
                return answer
            answer += 1
        else:
            queue.append((index, value))
    
    return answer