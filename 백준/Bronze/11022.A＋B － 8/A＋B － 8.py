T = int(input())
answer = []

for i in range(T):
    A, B = map(int, input().split())
    answer.append([A, B])

for i in range(T):
    print('Case #{}: {} + {} = {}'.format(i+1, answer[i][0], answer[i][1], sum(answer[i])))