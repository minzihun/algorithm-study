T = int(input())
answer = []

for i in range(T):
    x, y = map(int, input().split())
    answer.append(x+y)

for e in answer:
    print(e)