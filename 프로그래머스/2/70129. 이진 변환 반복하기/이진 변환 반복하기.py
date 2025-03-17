def solution(s):
    
    change = 0
    count = 0
    
    while (len(s) > 1):
        new = s.replace("0","")
        change += 1
        count += (len(s) - len(new))
        s = format(len(new),"b")
    
    answer = [change, count]
    return answer