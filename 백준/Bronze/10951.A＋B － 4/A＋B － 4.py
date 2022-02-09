import sys

answer = []
while(True):
    try:
        a, b = map(int, input().split())
        answer.append(a+b)
    except:
        break

for i in range(len(answer)):
    print(answer[i])