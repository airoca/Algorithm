def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    numbers.sort(key = lambda x: x*10, reverse = True)
    
    for n in numbers:
        answer += n
    
    if answer[0] == "0":
        return "0"
    
    return answer