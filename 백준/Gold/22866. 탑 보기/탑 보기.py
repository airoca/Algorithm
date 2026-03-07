n = int(input())
heights = list(map(int, input().split()))

count = [0]*n
nearest = [-1]*n
stack = []

# 왼쪽 -> 오른쪽
for i in range(n):
    h = heights[i]

    while stack and heights[stack[-1]] <= h:
        stack.pop()

    count[i] += len(stack)

    if stack:
        nearest[i] = stack[-1]

    stack.append(i)

stack = []

# 오른쪽 -> 왼쪽
for i in range(n-1, -1, -1):
    h = heights[i]

    while stack and heights[stack[-1]] <= h:
        stack.pop()

    count[i] += len(stack)

    if stack:
        if nearest[i] == -1 or abs(i-stack[-1]) < abs(i-nearest[i]):
            nearest[i] = stack[-1]

    stack.append(i)

for i in range(n):
    if count[i] == 0:
        print(0)
    else:
        print(count[i], nearest[i]+1)