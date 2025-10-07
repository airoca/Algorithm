def solution(s):
    answer = []
    lst = s.split("},")
    
    for i in range(len(lst)):
        lst[i] = lst[i].strip("{}").split(",")
        lst[i] = list(map(int, lst[i]))
    
    lst.sort(key=len)
    
    for s in lst:
        for number in s:
            if number not in answer:
                answer.append(number)
    
    return answer