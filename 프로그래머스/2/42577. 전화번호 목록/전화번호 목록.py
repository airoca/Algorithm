def solution(phone_book):
    
    phone_book.sort(key = lambda x: len(x), reverse = True)
    
    d = {}
    
    for number in phone_book:
        if number in d:
            return False
        for i in range(1,len(number)+1):
            string = number[:i]
            d[string] = 1
    
    return True