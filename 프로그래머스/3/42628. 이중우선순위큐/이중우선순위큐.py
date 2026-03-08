import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)
    
    idx = 0
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1
            
        elif num == 1:
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
            
        else:
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    if not min_heap:
        answer = [0,0]
    else:
        answer = [-max_heap[0][0], min_heap[0][0]]
    
    return answer