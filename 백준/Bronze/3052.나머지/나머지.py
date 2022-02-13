answer = []

for i in range(10):
    temp = int(input())
    temp = temp%42
    answer.append(temp)

answer = list(set(answer))

print(len(answer))