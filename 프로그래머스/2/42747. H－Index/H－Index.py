def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    
    return answer