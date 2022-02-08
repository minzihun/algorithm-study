import sys

T = int(sys.stdin.readline())
answer = []

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    answer.append(a+b)

for i in range(T):
    print(answer[i])