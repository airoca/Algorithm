def solution(answers):
    answer = []
    
    count = [0, 0, 0]
    a1 = [1,2,3,4,5] * 2000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    a_list = [a1, a2, a3]
    
    for i in range(len(answers)):
        for k in range(3):
            if a_list[k][i] == answers[i]:
                count[k] += 1
    
    max_val = max(count)
    
    for i in range(3):
        if count[i] == max_val:
            answer.append(i+1)
    
    return answer