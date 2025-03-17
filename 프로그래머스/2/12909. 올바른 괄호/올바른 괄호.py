def solution(s):
    
    lst = []
    
    for cur in s:
        if cur == "(":
            lst.append(cur)
        else:
            if len(lst) == 0:
                return False
            lst.pop()
    
    if len(lst) != 0:
        return False

    return True