from itertools import permutations

def solution(expression):
    ops = []
    nums = []
    number = ""
    result = 0
    
    for c in expression:
        if c.isdigit():
            number += c
        else:
            nums.append(number)
            ops.append(c)
            number = ""
    nums.append(number)
    
    ops_set = list(set(ops))
    ops_per = list(permutations(ops_set))
    
    for cur_per in ops_per:
        temp_ops = ops[::]
        temp_nums = nums[::]
        for cur_ops in cur_per:
            i = 0
            while i < len(temp_ops):
                if temp_ops[i] == cur_ops:
                    temp_nums[i] = str(eval(temp_nums[i] + cur_ops + temp_nums[i+1]))
                    del temp_nums[i+1]
                    del temp_ops[i]
                else:
                    i += 1
        result = max(result, abs(int(temp_nums[0])))
            
    return result