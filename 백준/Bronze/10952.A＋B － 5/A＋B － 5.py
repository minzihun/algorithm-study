answer = []
while(True):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    answer.append(a+b)

for i in range(len(answer)):
    print(answer[i])