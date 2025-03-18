def solution(elements):
    
    counts = set()
    length = len(elements)
    elements = elements * 2
    
    for count in range(length):
        for start in range(len(elements)):
            counts.add(sum(elements[start:start+count+1]))
    
    return len(counts)