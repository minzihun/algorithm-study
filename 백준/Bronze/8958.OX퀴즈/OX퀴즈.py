n = int(input())
answer = []

for i in range(n):
    temp = input()
    cnt = 0
    check = 1
    
    for j in range(len(temp)):
        
        if j > 0 and temp[j-1] == 'O':
            check += 1
        else:
            check = 1
        
        if temp[j] == 'O':
            cnt += check
    
    answer.append(cnt)

for e in answer:
    print(e)