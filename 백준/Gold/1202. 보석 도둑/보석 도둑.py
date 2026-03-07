import heapq
import sys

input = sys.stdin.readline

len_gems, len_bags = map(int, input().split())

gems = []
bags = []
answer = 0

for _ in range(len_gems):
    gems.append(list(map(int, input().split())))

for _ in range(len_bags):
    bags.append(int(input()))

gems.sort()
bags.sort()

i = 0
heap = []

for b in bags:
    while i < len_gems and b >= gems[i][0]:
        heapq.heappush(heap, -gems[i][1])
        i += 1
    if heap:
        answer -= heapq.heappop(heap)

print(answer)