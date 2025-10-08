def solution(cap, n, deliveries, pickups):
    answer = 0
    needD = 0
    needP = 0

    for i in range(n-1, -1, -1):
        needD += deliveries[i]
        needP += pickups[i]

        while needD > 0 or needP > 0:
            needD -= cap
            needP -= cap
            answer += (i + 1) * 2
            
    return answer