def solution(s):
    
    # 숫자에 대응되는 영단어 딕셔너리 생성
    eng_num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
                   'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    # 딕셔너리리 아이템이랑 문자열 s에 일치 하는 것이 있으면 숫자로 대치
    for i in eng_num_dic.keys():
        try:
            s = s.replace(i, eng_num_dic[i])
        except ValueError:
            pass 
         
    # 숫자로 이뤄진 문자열 숫자로 변환
    answer = int(s)
    
    return answer