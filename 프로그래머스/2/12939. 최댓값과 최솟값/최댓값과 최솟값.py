def solution(s):
    lst = list(map(int, s.split(" ")))
    answer = str(min(lst)) + " " + str(max(lst))
    return answer