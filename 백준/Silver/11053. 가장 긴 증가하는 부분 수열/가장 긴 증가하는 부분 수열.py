import bisect

n = int(input())
lst = list(map(int,input().split()))
result = [lst[0]]

for num in lst:
    if num>result[-1]:
        result.append(num)
    else:
        idx = bisect.bisect_left(result, num)
        result[idx] = num

print(len(result))