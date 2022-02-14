c = int(input())
answer = []

for i in range(c):
    temp = list(map(int, input().split()))
    total = temp.pop(0)
    avg = sum(temp)/total
    cnt = 0
    
    for e in temp:
        if e > avg:
            cnt += 1
    
    ratio = (cnt/total) * 100
    
    answer.append(round(ratio, 3))

for e in answer:
    print('{:.3f}%'.format(e))