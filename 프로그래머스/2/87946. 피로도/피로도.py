from itertools import permutations

def solution(k, dungeons):
    answer = -1
    perms = list(permutations(dungeons))
    
    for dungeon in perms:
        temp = 0
        cur = k
        for req, minus in dungeon:
            if cur >= req:
                temp += 1
                cur -= minus
            else:
                break
        answer = max(answer, temp)
    
    return answer