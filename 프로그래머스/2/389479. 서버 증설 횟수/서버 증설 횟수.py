import math

def solution(players, m, k):
    answer = 0
    time = len(players)
    server = 0
    expired_server = [0] * time
    
    for i in range(time):
        server -= expired_server[i]
        required_server = math.floor(players[i] / m)
        if required_server > server:
            required = required_server - server
            server += required
            answer += required
            if (i+k) < time:
                expired_server[i+k] = required
        
    return answer
