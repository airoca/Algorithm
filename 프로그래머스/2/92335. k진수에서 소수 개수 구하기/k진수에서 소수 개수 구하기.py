def solution(n, k):
    answer = 0
    base_k = ""
    
    while n > 0:
        base_k = str(n % k) + base_k
        n //= k

    candidates = base_k.split('0')
    
    for c in candidates:
        if c == "":
            continue 
        num = int(c)
        if is_prime(num):
            answer += 1

    return answer

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True