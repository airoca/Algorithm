import heapq

def solution(jobs):
    answer = 0
    time = 0
    i = 0
    heap = []
    
    jobs.sort()
    
    while heap or i < len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if not heap:
            time = jobs[i][0]
            continue
        
        dur, start = heapq.heappop(heap)
        time += dur
        answer += (time - start)
    
    return answer // len(jobs)