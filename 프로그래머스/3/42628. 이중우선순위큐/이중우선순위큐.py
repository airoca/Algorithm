import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for op in operations:
        op1, op2 = op.split()
        op2 = int(op2)
        if op1 == "I":
            heapq.heappush(min_heap, op2)
            heapq.heappush(max_heap, -op2)
        else:
            if not min_heap:
                continue
            elif len(min_heap) == 1:
                min_heap.pop()
                max_heap.pop()
            elif op2 == 1:
                max_val = heapq.heappop(max_heap)
                min_heap.remove(-max_val)
            else:
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
    
    if not min_heap:
        answer = [0,0]
    else:
        max_val = heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        answer = [-max_val, min_val]
    
    return answer