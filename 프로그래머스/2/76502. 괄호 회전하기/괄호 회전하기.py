def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if validate(s):
            answer += 1
    return answer

def validate(s):
    stack = []
    for c in s:
        if c in "[{(":
            stack.append(c)
        else:
            if not stack:
                return False
            cur = stack.pop()
            if (
                (c == "]" and cur != "[") or
                (c == "}" and cur != "{") or
                (c == ")" and cur != "(")
            ):
                return False
    return not stack