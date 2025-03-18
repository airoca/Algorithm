def solution(s):
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
        elif letter == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    
    if not stack:
        return 1
    else:
        return 0
    
    