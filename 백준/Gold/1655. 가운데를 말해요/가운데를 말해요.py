import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap1 = []
heap2 = []

for i in range(n):
    cur = int(input())

    if len(heap2) == 0:
        heapq.heappush(heap2, cur)
        print(cur)
        continue
    
    mid = heap2[0]

    if cur > mid:
        heapq.heappush(heap2, cur)
    else:
        heapq.heappush(heap1, -cur)

    if len(heap1) - len(heap2) > 1:
        move = heapq.heappop(heap1)
        heapq.heappush(heap2, -move)
    elif len(heap2) - len(heap1) > 1:
        move = heapq.heappop(heap2)
        heapq.heappush(heap1, -move)

    if len(heap1) < len(heap2):
        print(heap2[0])
    else:
        print(-heap1[0])