def solution(s):
    lst = s.split(" ")
    
    for i in range(len(lst)):
        if lst[i] == "":
            continue
        lst[i] = lst[i][0].upper() + lst[i][1:].lower()
        
    answer = " ".join(lst)
    
    return answer