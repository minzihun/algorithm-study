A = int(input())
B = int(input())
C = int(input())

cal = str(A*B*C)
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = []

for i in num_list:
    cnt = 0
    
    for j in cal:
        if i == int(j):
            cnt += 1
    
    answer.append(cnt)
    
for i in answer:
    print(i)