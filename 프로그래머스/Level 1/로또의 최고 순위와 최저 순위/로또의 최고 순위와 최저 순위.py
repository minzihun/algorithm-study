def solution(lottos, win_nums):
    
    answer = []
    
    cnt = 0
    cnt_zero = 0
    rank = [[6, 1], [5, 2], [4, 3], [3, 4], [2, 5], [1, 6], [0, 6]]
    
    for i in range(6):
        if lottos[i] == 0:
            cnt_zero += 1
            
        for j in range(6):
            if lottos[i] == win_nums[j]:
                cnt += 1
    
    for i in range(7):
        if (cnt+cnt_zero) == rank[i][0]:
            answer.append(rank[i][1])
            
        if cnt == rank[i][0]:
            answer.append(rank[i][1])
    
    return answer