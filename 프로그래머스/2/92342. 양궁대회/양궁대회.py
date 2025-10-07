def solution(n, info):
    max_diff = 0
    answer = [-1]
    
    def calc_diff(lion, apeach):
        lion_score, apeach_score = 0, 0
        for i in range(11):
            if lion[i] == 0 and apeach[i] == 0:
                continue
            if lion[i] > apeach[i]:
                lion_score += 10 - i
            else:
                apeach_score += 10 - i
        return lion_score - apeach_score

    def dfs(idx, arrows, lion_info):
        nonlocal max_diff, answer
        
        # 모든 점수를 다 돌았을 때
        if idx == 11:
            if arrows > 0:
                lion_info[10] += arrows  # 남은 화살은 0점에 몰아줌
            diff = calc_diff(lion_info, info)
            if diff > 0:  # 라이언이 이길 때만 고려
                if diff > max_diff:
                    max_diff = diff
                    answer = lion_info[:]
                elif diff == max_diff:
                    # 가장 낮은 점수를 더 많이 맞힌 경우 선택
                    for i in range(10, -1, -1):
                        if lion_info[i] > answer[i]:
                            answer = lion_info[:]
                            break
                        elif lion_info[i] < answer[i]:
                            break
            if arrows > 0:
                lion_info[10] -= arrows  # 원상복구
            return

        # 1️⃣ 해당 점수를 이기기 위해 쏨
        need = info[idx] + 1
        if need <= arrows:
            lion_info[idx] = need
            dfs(idx + 1, arrows - need, lion_info)
            lion_info[idx] = 0  # 백트래킹

        # 2️⃣ 해당 점수를 포기함
        dfs(idx + 1, arrows, lion_info)
    
    dfs(0, n, [0] * 11)
    return answer
