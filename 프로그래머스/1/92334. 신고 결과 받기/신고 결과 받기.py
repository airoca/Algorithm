def solution(id_list, report, k):
    
    answer = []
    id_dict = {}
    
    for id in id_list:
        # 신고당한 횟수, 신고한 사용자 id, 처리 결과 메일 수
        id_dict[id] = [0,[],0]
    
    for r in report:
        u_id, r_id = r.split()
        if u_id in id_dict[r_id][1]:
            continue
        id_dict[r_id][0] += 1
        id_dict[r_id][1].append(u_id)
        
    for id in id_dict:
        if id_dict[id][0] >= k:
            for u_id in id_dict[id][1]:
                id_dict[u_id][2] += 1
    
    for id in id_dict:
        answer.append(id_dict[id][2])
    
    return answer