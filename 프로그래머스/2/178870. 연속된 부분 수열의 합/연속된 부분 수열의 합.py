def solution(sequence, k):
    
    left, right, result = 0, 0, 0
    length = 1000000
    answer = []
    
    while right < len(sequence):
        result += sequence[right]
        while result > k and left <= right:
            result -= sequence[left]
            left += 1
        if result == k and right - left < length:
            length = right - left
            answer = [left, right]
        right += 1
    
    return answer