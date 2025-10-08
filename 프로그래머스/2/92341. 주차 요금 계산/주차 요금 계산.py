import math

def solution(fees, records):
    
    d_time = {}
    d_result_time = {}
    d_price = {}
    answer = []
    
    for record in records:
        time, car, flag = record.split()
        if flag == "IN":
            d_time[car] = time
        elif flag == "OUT":
            in_time = d_time[car]
            result_time = calculate_time(in_time, time)
            del d_time[car]
            if car in d_result_time:
                d_result_time[car] += result_time
            else:
                d_result_time[car] = result_time

    # 나머지 차 정리
    for car in d_time:
        in_time = d_time[car]
        result_time = calculate_time(in_time, "23:59")
        if car in d_result_time:
            d_result_time[car] += result_time
        else:
            d_result_time[car] = result_time
    
    for car in d_result_time:
        d_price[car] = calculate_price(fees, d_result_time[car])
    
    for key in sorted(d_price.keys()):
        answer.append(d_price[key])
    
    return answer

def calculate_time(in_time, out_time):
    in_hour, in_min = in_time.split(":")
    out_hour, out_min = out_time.split(":")
    in_total = int(in_hour) * 60 + int(in_min)
    out_total = int(out_hour) * 60 + int(out_min)
    return out_total - in_total

def calculate_price(fees, result_min):
    base_min, base_price, plus_min, plus_price = fees[0], fees[1], fees[2], fees[3]
    if result_min <= base_min:
        return base_price
    else:
        return base_price + math.ceil((result_min - base_min) / plus_min) * plus_price
    