import string

def solution(new_id):
    answer = ''
    
    lower = [i for i in string.ascii_lowercase]
    num = [str(i) for i in range(10)]
    special = ['-', '_', '.']
    rule = lower + num + special
    
    new_id = list(new_id.lower())
    
    re_new_id = []
    
    for i in range(len(new_id)):
        for j in range(len(rule)):
            if new_id[i] == rule[j]:
                re_new_id.append(new_id[i])
    
    merge_id = "".join(re_new_id)
    for i in range(len(merge_id)):
        merge_id = merge_id.replace("..", ".")
    merge_id = list(merge_id)
    
    if merge_id[0] == '.':
        del merge_id[0]
    
    if len(merge_id) > 1:
        if merge_id[-1] == '.':
            del merge_id[-1]

    if len(merge_id) == 0:
        merge_id.append('a')
    
    if len(merge_id) >= 16:
        temp = []
        
        for i in range(15):
            temp.append(merge_id[i])
        merge_id = temp
        
        if merge_id[14] == '.':
            del merge_id[14]
    
    elif len(merge_id) <= 2:
        for i in range(3):
            if len(merge_id) != 3:
                merge_id.append(merge_id[-1])
    
    answer = "".join(merge_id)
    return answer