n = int(input())
m = int(input())

parent = [i for i in range(n+1)]

def find_parent(c):
    if parent[c] != c:
        parent[c] = find_parent(parent[c])
    return parent[c]

def union(c1, c2):
    p1 = find_parent(c1)
    p2 = find_parent(c2)
    if p1 != p2: 
        parent[p2] = p1

for c1 in range(1, n+1):
    cities = list(map(int, input().split()))
    for i in range(n):
        if cities[i] == 0:
            continue
        c2 = i+1    
        if c1 < c2:
            union(c1, c2)
        else:
            union(c2, c1)

travel = list(map(int, input().split()))
root = find_parent(travel[0])
flag = True

for t in travel:
    if find_parent(t) != root:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")